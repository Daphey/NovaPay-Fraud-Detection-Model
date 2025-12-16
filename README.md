


#  NovaPay Fraud Detection System

This project is an end-to-end fraud detection prototype built using real-world payment transaction data. It covers data cleaning, exploratory data analysis, feature engineering, machine learning modeling, and deployment using Streamlit.

---

## Dataset Overview
The dataset contains **10,200 transactions** with features including:
- Transaction amount and fees
- Device and IP risk signals
- Customer behavior patterns
- Velocity indicators
- Internal and corridor risk scores

Target variable:
- `is_fraud` (1 = Fraud, 0 = Legitimate)

---

## Data Preparation
Key preprocessing steps:
- Missing value handling (median for numeric, 'unknown' for categorical)
- Datatype corrections
- Categorical standardization
- Log transformation for skewed monetary values
- Class imbalance handled using evaluation metrics (PR-AUC, Recall)

---

## Exploratory Data Analysis
Key insights:
- Fraud is highly imbalanced (~2%)
- Fraudulent transactions tend to:
  - Have higher amounts
  - Occur on new devices
  - Show higher IP and internal risk scores
  - Appear on younger accounts

---

##  Feature Engineering
Features engineered include:
- Time-based transaction velocity
- Device and location risk flags
- Log-transformed monetary values
- Encoded categorical features using OneHotEncoder

---

##  Models Trained
| Model | ROC-AUC | PR-AUC |
|-----|--------|-------|
| Logistic Regression | 0.67 | 0.05 |
| Random Forest | **0.70** | **0.09** |
| XGBoost | 0.69 | 0.05 |

 **Random Forest** was selected due to better minority-class detection.

---

##  Deployment (Streamlit App)

The project includes an interactive Streamlit UI that:
- Accepts transaction details
- Returns fraud probability
- Explains feature influence
