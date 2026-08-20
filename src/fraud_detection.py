import pandas as pd
import os

# -----------------------------
# 1. File paths
# -----------------------------
INPUT_FILE = "data/credit_card_fraud_4k.csv"
OUTPUT_FILE = "output/processed_transactions.csv"


# -----------------------------
# 2. Read dataset
# -----------------------------
print("Reading transaction dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Total transactions: {len(df)}")


# -----------------------------
# 3. Validate required columns
# -----------------------------
required_columns = [
    "transaction_id",
    "customer_id",
    "amount",
    "location",
    "transaction_hour",
    "previous_transaction_amount",
    "international"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}"
    )

print("Column validation successful.")


# -----------------------------
# 4. Handle missing values
# -----------------------------
df["amount"] = pd.to_numeric(
    df["amount"],
    errors="coerce"
)

df["previous_transaction_amount"] = pd.to_numeric(
    df["previous_transaction_amount"],
    errors="coerce"
)

df["transaction_hour"] = pd.to_numeric(
    df["transaction_hour"],
    errors="coerce"
)

df["international"] = pd.to_numeric(
    df["international"],
    errors="coerce"
)

# Remove rows with critical missing values
df = df.dropna(
    subset=[
        "transaction_id",
        "amount",
        "transaction_hour",
        "previous_transaction_amount",
        "international"
    ]
)


# -----------------------------
# 5. Initialize risk score
# -----------------------------
df["risk_score"] = 0

df["fraud_reason"] = ""


# -----------------------------
# 6. Rule 1: High transaction
# -----------------------------
high_amount = df["amount"] > 50000

df.loc[high_amount, "risk_score"] += 1

df.loc[high_amount, "fraud_reason"] += (
    "High transaction amount; "
)


# -----------------------------
# 7. Rule 2: International
# -----------------------------
international_transaction = df["international"] == 1

df.loc[
    international_transaction,
    "risk_score"
] += 1

df.loc[
    international_transaction,
    "fraud_reason"
] += "International transaction; "


# -----------------------------
# 8. Rule 3: Unusual transaction hour
# -----------------------------
unusual_hour = df["transaction_hour"] < 5

df.loc[unusual_hour, "risk_score"] += 1

df.loc[unusual_hour, "fraud_reason"] += (
    "Unusual transaction hour; "
)


# -----------------------------
# 9. Rule 4: Sudden amount increase
# -----------------------------
sudden_increase = (
    df["amount"]
    > df["previous_transaction_amount"] * 10
)

df.loc[sudden_increase, "risk_score"] += 1

df.loc[sudden_increase, "fraud_reason"] += (
    "Sudden increase from previous transaction; "
)


# -----------------------------
# 10. Assign risk category
# -----------------------------
def classify_risk(score):

    if score >= 3:
        return "High Risk"

    elif score == 2:
        return "Suspicious"

    else:
        return "Normal"


df["risk_category"] = df["risk_score"].apply(
    classify_risk
)


# -----------------------------
# 11. Clean fraud reason
# -----------------------------
df["fraud_reason"] = df["fraud_reason"].str.rstrip("; ")


# -----------------------------
# 12. Create output directory
# -----------------------------
os.makedirs("output", exist_ok=True)


# -----------------------------
# 13. Save processed dataset
# -----------------------------
df.to_csv(
    OUTPUT_FILE,
    index=False
)


# -----------------------------
# 14. Display summary
# -----------------------------
print("\n===== FRAUD DETECTION SUMMARY =====")

print(
    df["risk_category"]
    .value_counts()
)


print("\n===== TOTAL TRANSACTION AMOUNT =====")

print(
    df["amount"].sum()
)


print("\n===== HIGH RISK TRANSACTIONS =====")

print(
    len(
        df[df["risk_category"] == "High Risk"]
    )
)


print("\n===== PROCESSED FILE =====")

print(OUTPUT_FILE)

print("\nFraud detection completed successfully!")