# 🛡️ Credit Card Fraud Detection System

A Python-based **Credit Card Fraud Detection and Transaction Risk Analytics System** that analyzes financial transactions, assigns risk scores using predefined fraud indicators, categorizes transactions into **Normal, Suspicious, and High Risk**, and provides an interactive dashboard for monitoring and investigation.

## 🚀 Live Demo

📊 **[Open FraudGuard Detection Dashboard](https://fraudguard-detection-dashboard.streamlit.app)**

## 🌐 Project Links

- 📊 **Live Dashboard:** https://fraudguard-detection-dashboard.streamlit.app
- 💻 **Source Code:** https://github.com/khushichoudhary950/credit-card-fraud-detection

---

## 📌 Project Overview

Financial transactions can contain unusual patterns such as extremely high transaction amounts, international transactions, transactions occurring at unusual hours, or sudden increases compared with previous transactions.

This project provides a lightweight fraud detection system that identifies such patterns using a **rule-based risk scoring approach**.

The system:

- Processes transaction data using Python and Pandas
- Validates required transaction columns
- Calculates a fraud risk score
- Identifies predefined fraud indicators
- Categorizes transactions by risk level
- Generates a processed transaction dataset
- Runs automated tests using Pytest
- Provides an interactive Streamlit dashboard
- Supports cloud-based deployment
- Includes CI/CD configuration for AWS CodeBuild

---

## 🎯 Objectives

The main objectives of this project are:

1. Detect potentially suspicious credit card transactions.
2. Assign a risk score based on predefined transaction indicators.
3. Categorize transactions into different risk levels.
4. Provide an interactive dashboard for transaction analysis.
5. Automate testing of the fraud detection pipeline.
6. Prepare the project for cloud-based CI/CD integration.

---

## ⚙️ How Fraud Detection Works

This project uses **rule-based risk scoring rather than machine learning**.

Each transaction is evaluated against predefined conditions.

### Risk Indicators

| Indicator | Risk Score |
|---|---:|
| Transaction amount > 50,000 | +1 |
| International transaction | +1 |
| Transaction occurs before 5 AM | +1 |
| Current amount > 10× previous transaction amount | +1 |

The maximum possible score is **4**.

### Risk Classification

| Risk Score | Category |
|---:|---|
| 0–1 | 🟢 Normal |
| 2 | 🟡 Suspicious |
| 3–4 | 🔴 High Risk |

This approach provides a transparent and explainable fraud detection mechanism.

---

## 📊 Dataset

The project uses a transaction dataset containing information such as:

- Transaction ID
- Customer ID
- Transaction amount
- Transaction hour
- Previous transaction amount
- Domestic/International transaction information
- Location
- Risk score
- Fraud reason
- Risk category

The processed dataset is generated automatically by the fraud detection script.

---

## 📈 Dashboard

The project includes an interactive **Streamlit dashboard** for analyzing transaction risk.

### Dashboard Features

- 📊 Total transaction count
- 💰 Total transaction value
- 📈 Average transaction amount
- 🚨 High-risk transaction count
- 🟢 Normal transaction analysis
- 🟡 Suspicious transaction analysis
- 🔴 High-risk transaction analysis
- 🌍 Domestic vs International transaction analysis
- 🔍 Fraud indicator analysis
- ⚠️ High-risk transaction monitoring
- 📍 Location-based filtering
- 🔎 Risk-category filtering

The dashboard allows users to filter the dataset and investigate transactions interactively.

### Dashboard Deployment

The dashboard is deployed using **Streamlit Community Cloud** and is available through the live demo link above.

---

## 🏗️ Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   └── credit_card_fraud_4k.csv
│
├── output/
│   ├── dashboard.py
│   └── processed_transactions.csv
│
├── src/
│   └── fraud_detection.py
│
├── tests/
│   └── test_fraud_detection.py
│
├── requirements.txt
├── buildspec.yml
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Technologies Used

### Programming

- Python

### Data Processing

- Pandas

### Dashboard & Visualization

- Streamlit
- Plotly

### Testing

- Pytest

### Version Control

- Git
- GitHub

### Cloud / DevOps

- AWS
- AWS CodeBuild
- AWS CodePipeline
- Amazon S3
- Streamlit Community Cloud

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/khushichoudhary950/credit-card-fraud-detection.git
```

### 2. Enter the Project Directory

```bash
cd credit-card-fraud-detection
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

The required packages are:

```text
pandas
pytest
streamlit
plotly
```

---

## ▶️ Run Fraud Detection

Run the main fraud detection program:

```bash
python src/fraud_detection.py
```

The program processes the transaction dataset and generates:

```text
output/processed_transactions.csv
```

The terminal displays:

- Total transactions
- Risk category distribution
- Total transaction amount
- Number of high-risk transactions
- Processed output location

---

## 📊 Run the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run output/dashboard.py
```

The dashboard will open in your browser.

Alternatively, you can use the deployed version:

**[Open Live Dashboard](https://fraudguard-detection-dashboard.streamlit.app)**

---

## 🧪 Run Tests

Run the automated test suite:

```bash
pytest
```

The tests verify important parts of the system, including:

- Dataset availability
- Required columns
- Processed output
- Risk categories
- Risk score range
- High-risk transaction detection
- Valid transaction amounts

The current test suite contains **8 automated tests**.

Expected result:

```text
8 passed
```

---

## 🔄 CI/CD Workflow

The project includes a `buildspec.yml` file for automated execution through AWS CodeBuild.

The workflow performs:

```text
GitHub
   │
   ▼
AWS CodePipeline
   │
   ▼
AWS CodeBuild
   │
   ├── Install dependencies
   │
   ├── Run fraud detection
   │
   ├── Run automated tests
   │
   └── Generate processed output
```

This structure allows the fraud detection pipeline to be executed automatically as part of a CI/CD workflow.

---

## ☁️ Cloud Architecture

The project is designed to support a cloud-based architecture using AWS services.

```text
                 ┌─────────────────┐
                 │     GitHub      │
                 │ Source Control  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ AWS CodePipeline│
                 │      CI/CD      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  AWS CodeBuild  │
                 │ Build + Testing │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Fraud Detection │
                 │    Pipeline     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Amazon S3 /     │
                 │ Output Storage  │
                 └─────────────────┘
```

---

## 🔐 Risk Detection Example

Suppose a transaction has:

```text
Amount = ₹80,000
International = Yes
Transaction Hour = 2 AM
Previous Transaction = ₹5,000
```

The system evaluates the transaction against the predefined rules:

```text
Amount > 50,000
        +1

International transaction
        +1

Transaction before 5 AM
        +1

80,000 > 10 × 5,000
        +1
```

Final risk score:

```text
4
```

Therefore:

```text
Risk Category = High Risk
```

---

## 🧪 Testing

The project includes automated tests covering the main fraud detection pipeline.

Run:

```bash
pytest
```

The tests help ensure that changes to the detection pipeline do not break the existing functionality.

---

## 💡 Key Features

### Transparent Detection

The system uses clearly defined rules, making every risk classification explainable.

### Interactive Analytics

The Streamlit dashboard allows users to explore transaction data dynamically.

### Automated Testing

Pytest provides automated validation of the processing pipeline.

### CI/CD Ready

The project contains a CodeBuild configuration for automated execution.

### Cloud Deployment

The dashboard is publicly deployed through Streamlit Community Cloud.

### Modular Structure

The project separates:

- Data
- Detection logic
- Dashboard
- Tests
- Build configuration

This makes the project easier to maintain and extend.

---

## 🔮 Future Improvements

Possible future improvements include:

- Machine learning-based fraud detection
- Real-time transaction streaming
- AWS S3 integration
- AWS Lambda-based processing
- CloudWatch monitoring
- Automated fraud alerts
- Customer-level behavioral analysis
- Advanced transaction anomaly detection
- Authentication for the dashboard
- Role-based access control
- Real-time fraud monitoring
- Cloud deployment using AWS infrastructure

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Python programming
- Pandas data processing
- Rule-based fraud detection
- Data analytics
- Streamlit dashboard development
- Plotly visualization
- Automated testing with Pytest
- Git and GitHub
- CI/CD concepts
- AWS cloud architecture
- Cloud deployment
- Software project organization

---

## 👩‍💻 Author

**Khushi**

B.Tech – Information Technology
SKIT Jaipur

---

## 📄 License

This project is intended for educational and portfolio purposes.
