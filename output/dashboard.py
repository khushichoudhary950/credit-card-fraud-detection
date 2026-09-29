import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Credit Card Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# LOAD DATA
# dashboard.py and processed_transactions.csv are in the
# SAME output folder.
# ============================================================

DATA_PATH = Path(__file__).parent / "processed_transactions.csv"


@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

    # Make sure numeric columns have the correct types
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["transaction_hour"] = pd.to_numeric(
        df["transaction_hour"],
        errors="coerce"
    )
    df["previous_transaction_amount"] = pd.to_numeric(
        df["previous_transaction_amount"],
        errors="coerce"
    )
    df["international"] = pd.to_numeric(
        df["international"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["risk_score"] = pd.to_numeric(
        df["risk_score"],
        errors="coerce"
    ).fillna(0).astype(int)

    return df


df = load_data(DATA_PATH)


# ============================================================
# TITLE
# ============================================================

st.title("🛡️ Credit Card Fraud Detection Dashboard")

st.markdown(
    """
    **Cloud-Based Fraud Detection Analytics**

    Python • Amazon S3 • AWS Glue • Amazon Athena
    """
)

st.divider()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


# Risk category filter
risk_options = sorted(
    df["risk_category"]
    .dropna()
    .unique()
    .tolist()
)

selected_risk = st.sidebar.multiselect(
    "Risk Category",
    options=risk_options,
    default=risk_options
)


# Domestic / International filter
selected_transaction_type = st.sidebar.multiselect(
    "Transaction Type",
    options=["Domestic", "International"],
    default=["Domestic", "International"]
)


# Location filter
location_options = sorted(
    df["location"]
    .dropna()
    .unique()
    .tolist()
)

selected_locations = st.sidebar.multiselect(
    "Location",
    options=location_options,
    default=[]
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    df["risk_category"].isin(selected_risk)
]


if "Domestic" not in selected_transaction_type:
    filtered_df = filtered_df[
        filtered_df["international"] != 0
    ]

elif "International" not in selected_transaction_type:
    filtered_df = filtered_df[
        filtered_df["international"] == 0
    ]


if selected_locations:
    filtered_df = filtered_df[
        filtered_df["location"].isin(selected_locations)
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_transactions = len(filtered_df)

total_amount = filtered_df["amount"].sum()

average_amount = (
    filtered_df["amount"].mean()
    if total_transactions > 0
    else 0
)

high_risk_transactions = (
    filtered_df["risk_category"] == "High Risk"
).sum()

suspicious_transactions = (
    filtered_df["risk_category"] == "Suspicious"
).sum()


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )


with col2:
    st.metric(
        "Total Transaction Amount",
        f"${total_amount:,.2f}"
    )


with col3:
    st.metric(
        "Average Transaction Amount",
        f"${average_amount:,.2f}"
    )


with col4:
    st.metric(
        "High Risk Transactions",
        f"{high_risk_transactions:,}"
    )


st.divider()


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.subheader("🚨 Transaction Risk Distribution")

col1, col2 = st.columns(2)


with col1:

    risk_counts = (
        filtered_df["risk_category"]
        .value_counts()
        .rename_axis("risk_category")
        .reset_index(
            name="transaction_count"
        )
    )

    fig_risk = px.bar(
        risk_counts,
        x="risk_category",
        y="transaction_count",
        text="transaction_count",
        title="Risk Category Distribution"
    )

    fig_risk.update_traces(
        textposition="outside"
    )

    fig_risk.update_layout(
        xaxis_title="Risk Category",
        yaxis_title="Number of Transactions",
        showlegend=False
    )

    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )


# ============================================================
# DOMESTIC VS INTERNATIONAL
# ============================================================

with col2:

    international_risk = (
        filtered_df
        .groupby(
            [
                "risk_category",
                "international"
            ]
        )
        .size()
        .reset_index(
            name="transaction_count"
        )
    )

    international_risk[
        "transaction_type"
    ] = international_risk[
        "international"
    ].map(
        {
            0: "Domestic",
            1: "International"
        }
    )

    fig_int = px.bar(
        international_risk,
        x="risk_category",
        y="transaction_count",
        color="transaction_type",
        barmode="group",
        text="transaction_count",
        title="Domestic vs International Risk"
    )

    fig_int.update_layout(
        xaxis_title="Risk Category",
        yaxis_title="Number of Transactions"
    )

    st.plotly_chart(
        fig_int,
        use_container_width=True
    )


# ============================================================
# FRAUD REASONS
# ============================================================

st.divider()

st.subheader(
    "🔍 Top Fraud Detection Indicators"
)


reason_df = filtered_df[
    filtered_df["fraud_reason"].notna()
    &
    (
        filtered_df["fraud_reason"]
        .astype(str)
        .str.strip()
        != ""
    )
]


reason_counts = (
    reason_df["fraud_reason"]
    .value_counts()
    .head(10)
    .sort_values()
    .rename_axis("fraud_reason")
    .reset_index(
        name="occurrences"
    )
)


if len(reason_counts) > 0:

    fig_reason = px.bar(
        reason_counts,
        x="occurrences",
        y="fraud_reason",
        orientation="h",
        text="occurrences",
        title="Most Frequently Triggered Fraud Reasons"
    )

    fig_reason.update_traces(
        textposition="outside"
    )

    fig_reason.update_layout(
        xaxis_title="Occurrences",
        yaxis_title="Fraud Reason"
    )

    st.plotly_chart(
        fig_reason,
        use_container_width=True
    )

else:

    st.info(
        "No fraud reasons match the selected filters."
    )


# ============================================================
# INTERNATIONAL RISK ANALYSIS
# ============================================================

st.divider()

st.subheader(
    "🌍 International Transaction Risk Analysis"
)


international_summary = (
    filtered_df
    .groupby(
        [
            "international",
            "risk_category"
        ]
    )
    .agg(
        transaction_count=(
            "transaction_id",
            "count"
        ),
        total_amount=(
            "amount",
            "sum"
        )
    )
    .reset_index()
)


international_summary[
    "transaction_type"
] = international_summary[
    "international"
].map(
    {
        0: "Domestic",
        1: "International"
    }
)


st.dataframe(
    international_summary[
        [
            "transaction_type",
            "risk_category",
            "transaction_count",
            "total_amount"
        ]
    ],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# HIGH-RISK TRANSACTIONS
# ============================================================

st.divider()

st.subheader(
    "⚠️ Top High-Risk Transactions"
)


high_risk_df = (
    filtered_df[
        filtered_df["risk_category"]
        == "High Risk"
    ]
    .sort_values(
        "amount",
        ascending=False
    )
    .head(20)
)


display_columns = [
    "transaction_id",
    "customer_id",
    "amount",
    "location",
    "transaction_hour",
    "previous_transaction_amount",
    "international",
    "risk_score",
    "fraud_reason",
    "risk_category"
]


if len(high_risk_df) > 0:

    st.dataframe(
        high_risk_df[
            display_columns
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "amount": st.column_config.NumberColumn(
                "Amount",
                format="$%.2f"
            ),

            "previous_transaction_amount":
                st.column_config.NumberColumn(
                    "Previous Amount",
                    format="$%.2f"
                ),

            "risk_score":
                st.column_config.NumberColumn(
                    "Risk Score"
                )
        }
    )

else:

    st.info(
        "No High Risk transactions match the selected filters."
    )


# ============================================================
# SUMMARY
# ============================================================

st.divider()

st.subheader("📌 Fraud Detection Summary")

normal_count = (
    filtered_df["risk_category"]
    == "Normal"
).sum()

suspicious_count = (
    filtered_df["risk_category"]
    == "Suspicious"
).sum()

st.write(
    f"""
    - **Total transactions:** {total_transactions:,}
    - **Normal transactions:** {normal_count:,}
    - **Suspicious transactions:** {suspicious_count:,}
    - **High-risk transactions:** {high_risk_transactions:,}
    - **Total transaction amount:** ${total_amount:,.2f}
    - **Average transaction amount:** ${average_amount:,.2f}
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Credit Card Fraud Detection Project | "
    "Python + Amazon S3 + AWS Glue + Amazon Athena"
)