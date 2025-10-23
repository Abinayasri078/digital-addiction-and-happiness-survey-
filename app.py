import streamlit as st
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Digital Addiction & Happiness Dashboard", layout="wide")
st.title("📱 Digital Addiction & Happiness Prediction Dashboard")

# === Put your verified raw GitHub URL here (exact) ===
url ="https://raw.githubusercontent.com/Abinayasri078/digital-addiction-and-happiness-survey/main/digital_addiction_happiness_300.xlsx"
pd.read_excel()
gh repo clone Abinayasri078/digital-addiction-and-happiness-survey-


# Check URL before trying to read
try:
    resp = requests.head(url, allow_redirects=True, timeout=10)
    if resp.status_code != 200:
        st.error(f"Failed to load data: HTTP Error {resp.status_code}. Check the raw file URL and repo visibility.")
        st.write("Expected raw URL format example:")
        st.code("https://github.com/<username>/<repo>/raw/main/<filename>.xlsx")
        st.stop()
except Exception as e:
    st.error("Could not reach the dataset URL. Check your internet/URL.")
    st.write(e)
    st.stop()

# Read Excel using openpyxl engine
try:
    df = pd.read_excel(url, engine="openpyxl")
    st.success("✅ Dataset loaded successfully")
    st.dataframe(df.head())
except Exception as e:
    st.error("Failed to read Excel file from the URL.")
    st.write(e)
    st.stop()

# ... rest of your app code below ...

