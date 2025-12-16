
import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
model = joblib.load("random_forest_fraud_model.pkl")
#preprocessor = joblib.load("preprocessor.pkl")

st.subheader("🔍 Feature Interpretation")

st.markdown("""
**How to interpret the inputs:**

- **Transaction Amount**: Larger amounts are generally higher risk.
- **Transaction Velocity (1h / 24h)**: Many transactions in a short time may indicate fraud.
- **Account Age**: New accounts are statistically more risky.
- **IP Risk Score**: Higher values indicate suspicious IP behavior.
- **Internal Risk Score**: NovaPay’s internal risk assessment.
- **New Device**: First-time device usage increases fraud likelihood.
- **Location Mismatch**: IP country differs from home country.
- **KYC Tier**: Higher tiers usually indicate more trusted users.
""")


st.set_page_config(page_title="NovaPay Fraud Detection", layout="centered")

st.title("🚨 NovaPay Fraud Detection System")
st.write("Enter transaction details to assess fraud risk.")

# --- User Inputs ---
amount_usd = st.number_input("Transaction Amount (USD)", min_value=0.0)
txn_velocity_1h = st.number_input("Transactions in last 1 hour", min_value=0)
txn_velocity_24h = st.number_input("Transactions in last 24 hours", min_value=0)
account_age_days = st.number_input("Account Age (days)", min_value=0)
ip_risk_score = st.slider("IP Risk Score", 0.0, 1.0)
risk_score_internal = st.slider("Internal Risk Score", 0.0, 1.0)

channel = st.selectbox("Channel", ["web", "mobile", "api"])
new_device = st.selectbox("New Device?", [True, False])
location_mismatch = st.selectbox("Location Mismatch?", [True, False])
kyc_tier = st.selectbox("KYC Tier", ["tier_1", "tier_2", "tier_3"])

# --- Build Input DataFrame ---
input_df = pd.DataFrame([{
    "amount_usd": amount_usd,
    "txn_velocity_1h": txn_velocity_1h,
    "txn_velocity_24h": txn_velocity_24h,
    "account_age_days": account_age_days,
    "ip_risk_score": ip_risk_score,
    "risk_score_internal": risk_score_internal,
    "channel": channel,
    "new_device": new_device,
    "location_mismatch": location_mismatch,
    "kyc_tier": kyc_tier
}])

# --- Prediction ---
if st.button("Check Fraud Risk"):
    X_processed = preprocessor.transform(input_df)
    fraud_prob = model.predict_proba(X_processed)[0][1]

    st.metric("Fraud Probability", f"{fraud_prob:.2%}")

    if fraud_prob > 0.5:
        st.error("⚠️ High Fraud Risk")
    else:
        st.success("✅ Low Fraud Risk")
