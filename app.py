import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Digital Addiction & Happiness Dashboard", layout="wide")
st.title("📱 Digital Addiction & Happiness Prediction Dashboard")

# Load dataset directly from GitHub (raw link)
url = "https://raw.githubusercontent.com/Abinayasri078/digital-addiction-and-happiness-survey/main/digital_addiction_happiness_300.xlsx"
df = pd.read_excel(url)

st.success("✅ Data loaded successfully!")
st.dataframe(df.head())

# Encode text data
df_clean = df.copy()
le = LabelEncoder()
for col in df_clean.columns:
    if df_clean[col].dtype == 'object':
        df_clean[col] = le.fit_transform(df_clean[col].astype(str))

# Create target variable (Happy vs Unhappy)
df_clean["Target"] = df[" HOW DO YOU USUALLY FEEL AFTER SPENDING TIME ON SOCIAL MEDIA ? "].apply(
    lambda x: 1 if str(x).strip().lower() in ["happy", "relaxed"] else 0
)

X = df_clean.drop(["Timestamp", "Email Address", "Target"], axis=1, errors='ignore')
y = df_clean["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
st.metric("🎯 Model Accuracy", f"{accuracy*100:.2f}%")

# Social Media Insights
st.header("📊 Social Media Usage Insights")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Screen Time")
    st.bar_chart(df["ON AVERAGE , HOW MANY HOURS DO YOU SPEND ON SOCIAL MEDIA DAILY ?"].value_counts())

with col2:
    st.subheader("Purpose of Social Media Use")
    st.bar_chart(df["WHAT IS YOUR PRIMARY PURPOSE FOR SOCIAL MEDIA ?"].value_counts())

# Prediction Section
st.header("🧠 Happiness Prediction")
col1, col2, col3 = st.columns(3)
screen_time = col1.selectbox("Social Media Hours", ["<1 hour","1-3 hours","3-5 hours","5-7 hours","7+ hours"])
fomo = col2.selectbox("FOMO Level", ["Strongly Disagree","Disagree","Neutral","Agree","Strongly Agree"])
stress = col3.selectbox("Stress Level", ["Strongly Disagree","Disagree","Neutral","Agree","Strongly Agree"])

input_df = pd.DataFrame({
    "ON AVERAGE , HOW MANY HOURS DO YOU SPEND ON SOCIAL MEDIA DAILY ?":[screen_time],
    "I FEAR THAT MY  FRIENDS ARE HAVING MORE FUN WITHOUT ME.":[fomo],
    "I GET STRESSED EASILY":[stress]
})

for col in input_df.columns:
    input_df[col] = le.fit_transform(input_df[col].astype(str))

pred = model.predict(input_df)[0]
if pred == 1:
    st.success("😊 You seem HAPPY! Keep maintaining healthy habits.")
else:
    st.error("😞 You seem UNHAPPY. Try a 30-min no-phone bedtime routine or reduce screen time.")


url = "https://github.com/Abinayasri078/digital-addiction-and-happiness-survey/raw/main/digital_addiction_happiness_300.xlsx"

