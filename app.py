import streamlit as st
from agent import analyze_and_heal_incident

st.set_page_config(page_title="CloudSentinel AI", layout="wide")

st.title("🛡️ CloudSentinel AI — Autonomous Incident Self-Healing Swarm")
st.caption("Powered by Gemini 1.5 Pro & Google Cloud Platform")

st.subheader("Simulate Infrastructure Security Incident")

sample_logs = {
    "IAM Policy Breach": "ALERT: Unauthorized service account created with 'roles/owner' privileges from IP 192.0.2.45",
    "Cloud Run Misconfiguration": "ERROR: Cloud Run service 'prod-api' public ingress exposed without authentication requirement.",
    "SQL Injection Attack": "WARNING: High number of malicious payloads detected in Cloud Armor logs targeting DB proxy."
}

selected_option = st.selectbox("Select Incident Scenario to Test:", list(sample_logs.keys()))
custom_log = st.text_area("Or Paste Raw Cloud Logging Payload:", value=sample_logs[selected_option])

if st.button("Trigger Autonomous Agent Swarm 🚀"):
    with st.spinner("Multi-Agent Swarm Active: Analyzing -> Generating Patch -> Sandboxing Fix..."):
        try:
            report = analyze_and_heal_incident(custom_log)
            st.success("Remediation Complete!")
            st.markdown(report)
        except Exception as e:
            st.error(f"Error running agents: {str(e)}")