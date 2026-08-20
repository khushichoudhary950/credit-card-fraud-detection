import pandas as pd


INPUT_FILE = "data/credit_card_fraud_4k.csv"
OUTPUT_FILE = "output/processed_transactions.csv"


def test_input_dataset_exists():
    df = pd.read_csv(INPUT_FILE)

    assert len(df) > 0


def test_required_columns_exist():

    df = pd.read_csv(INPUT_FILE)

    required_columns = [
        "transaction_id",
        "customer_id",
        "amount",
        "location",
        "transaction_hour",
        "previous_transaction_amount",
        "international"
    ]

    for column in required_columns:
        assert column in df.columns


def test_processed_file_exists():

    df = pd.read_csv(OUTPUT_FILE)

    assert len(df) > 0


def test_risk_columns_exist():

    df = pd.read_csv(OUTPUT_FILE)

    assert "risk_score" in df.columns
    assert "risk_category" in df.columns
    assert "fraud_reason" in df.columns


def test_risk_categories_are_valid():

    df = pd.read_csv(OUTPUT_FILE)

    valid_categories = {
        "Normal",
        "Suspicious",
        "High Risk"
    }

    assert set(df["risk_category"]).issubset(
        valid_categories
    )


def test_risk_score_is_valid():

    df = pd.read_csv(OUTPUT_FILE)

    assert df["risk_score"].min() >= 0
    assert df["risk_score"].max() <= 4


def test_high_risk_transactions_exist():

    df = pd.read_csv(OUTPUT_FILE)

    high_risk_count = (
        df["risk_category"] == "High Risk"
    ).sum()

    assert high_risk_count > 0


def test_transaction_amounts_are_valid():

    df = pd.read_csv(INPUT_FILE)

    assert (df["amount"] >= 0).all()