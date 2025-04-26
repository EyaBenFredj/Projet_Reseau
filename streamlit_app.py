import streamlit as st
import requests

st.set_page_config(page_title="Network Optimizer", layout="centered")

st.title("🔗 Network Synchronization Optimizer")

# Input fields
site_id = st.text_input("🌐 Site ID", "siteA")
bandwidth = st.number_input("📶 Network Bandwidth (Mbps)", min_value=0.0, step=0.1)
latency = st.number_input("⏱️ Network Latency (ms)", min_value=0.0, step=1.0)

# Submit button
if st.button("🚀 Get Optimization Recommendation"):
    payload = {
        "site_id": site_id,
        "bandwidth": bandwidth,
        "latency": latency
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_code == 200:
            recommendation = response.json()["recommendation"]
            st.success(f"✅ Recommended Strategy: **{recommendation}**")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to the FastAPI backend. Is it running?")