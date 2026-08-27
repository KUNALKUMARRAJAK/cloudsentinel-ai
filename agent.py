import os
import google.generativeai as genai

# API key setup from environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def analyze_and_heal_incident(error_log: str):
    prompt = f"""
    You are CloudSentinel AI, an autonomous multi-agent cloud security system.
    Analyze the following Google Cloud infrastructure log/incident and perform remediation:
    
    LOG PAYLOAD:
    "{error_log}"
    
    Return a structured markdown report containing:
    1. **Incident Severity & Threat Type**
    2. **Root Cause Analysis**
    3. **Autonomous Remediation Code (Terraform or Python GCP SDK Script)**
    4. **Verification Status (Dry-run Sandbox Execution Result)**
    """
    
    # Smart Fallback Mechanism for Free Tier Daily Quota (Using fresh models)
    try:
        model = genai.GenerativeModel('gemini-3.7-flash')
        response = model.generate_content(prompt)
    except Exception as e:
        # Fallback to alternative fresh model if daily limit triggers
        model = genai.GenerativeModel('gemini-3.5-flash')
        response = model.generate_content(prompt)
        
    return response.text