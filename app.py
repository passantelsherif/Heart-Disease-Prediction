# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load("heart_disease_model.pkl")  

# Streamlit page setup
st.set_page_config(page_title="Heart Disease Risk Checker", layout="wide")
st.title("Heart Disease Risk Checker")
st.markdown("This tool helps assess the likelihood of heart disease based on medical data. Fill in the information on the sidebar.")

# Sidebar form
st.sidebar.header("🔧 Patient Information")

def user_input_features():
    with st.sidebar.form(key="input_form"):
        age = st.slider("Age", 20, 100, 50)
        sex = st.radio("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 240)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["No", "Yes"])
        restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
        exang = st.radio("Exercise Induced Angina?", ["No", "Yes"])
        oldpeak = st.slider("ST Depression Induced", 0.0, 6.0, 1.0, step=0.1)
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
        ca = st.slider("Number of Major Vessels (0–3)", 0, 3, 0)
        thal = st.selectbox("Thalassemia", ["Normal (3)", "Fixed Defect (6)", "Reversible Defect (7)"])

        submit = st.form_submit_button("Predict")

    # Encode categorical inputs
    sex = 1 if sex == "Male" else 0
    cp = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}[cp]
    fbs = 1 if fbs == "Yes" else 0
    restecg = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}[restecg]
    exang = 1 if exang == "Yes" else 0
    slope = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[slope]
    thal = {"Normal (3)": 3, "Fixed Defect (6)": 6, "Reversible Defect (7)": 7}[thal]

    data = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
        'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
        'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
    }
    return pd.DataFrame(data, index=[0]), submit

input_df, submitted = user_input_features()

# Show input and result
if submitted:
    st.subheader("🩺 Patient Data")
    st.dataframe(input_df)

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    st.subheader("🔍 Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease!")
    else:
        st.success("✅ Low risk of heart disease!")

    st.subheader("📊 Prediction Probability")

    st.write(f"**Probability of Heart Disease:** `{proba[1]:.2f}`")
    st.write(f"**Probability of No Heart Disease:** `{proba[0]:.2f}`")

    # Risk Threshold
    risk = proba[1]
    risk_color = "#FF4B4B" if risk > 0.5 else "#6EB52F"  # Red if risky, Green otherwise

    # Custom styled progress bar
    st.markdown(
        f"""
        <div style="margin-top: 10px; margin-bottom: 5px;"> 
            <strong>Risk Indicator:</strong>
            <div style="background-color: #e0e0e0; border-radius: 10px; height: 20px; width: 100%;">
                <div style="
                    width: {risk * 100}%;
                    background-color: {risk_color};
                    height: 100%;
                    border-radius: 10px;">
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    with st.expander("📈 Show Sample Chart: Risk Probability Bar"):
        fig, ax = plt.subplots()
        sns.barplot(x=["No Disease", "Disease"], y=proba, palette="Set2", ax=ax)
        ax.set_ylabel("Probability")
        ax.set_title("Heart Disease Risk")
        st.pyplot(fig)
