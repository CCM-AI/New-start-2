import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# Streamlit Title and Description
st.title("Chronic Care Management System")
st.subheader("Using AI and Evidence-Based Guidelines for Sustainable Chronic Condition Management")

# Introduction
st.write("""
This platform supports patients and healthcare providers by leveraging evidence-based chronic care practices.
Through AI-driven insights, personalized care plans, and self-management support, we aim to reduce the impact 
of chronic conditions while enhancing outcomes sustainably.
""")

# 1️⃣ Patient Input Data
st.header("1. Patient Input Data")
st.write("Provide patient details to assess risk and personalize care plans.")

# Collect patient information
with st.form(key="patient_form"):
    patient_data = {
        "age": st.number_input("Age", min_value=0, max_value=120, value=45),
        "weight": st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0),
        "height": st.number_input("Height (cm)", min_value=0, max_value=250, value=170),
        "blood_pressure": st.slider("Blood Pressure (mm Hg)", 80, 200, 120),
        "cholesterol": st.slider("Cholesterol Level (mg/dL)", 100, 300, 180),
        "diabetes": st.selectbox("Diabetes Status", ["No", "Yes"]),
        "smoking": st.selectbox("Smoking Status", ["Non-smoker", "Former smoker", "Current smoker"]),
        "physical_activity": st.selectbox("Physical Activity Level", ["Sedentary", "Moderate", "Active"])
    }
    submit_button = st.form_submit_button(label="Submit Patient Data")

# Calculate BMI
if submit_button:
    patient_data["bmi"] = patient_data["weight"] / ((patient_data["height"] / 100) ** 2)
    st.write(f"Calculated BMI: {patient_data['bmi']:.2f}")

# 2️⃣ AI-Driven Risk Stratification
st.header("2. AI-Driven Risk Stratification")
st.write("Assess the patient's risk for chronic conditions based on input data using AI insights.")

# Sample dataset and model training (Replace this with a real model trained on evidence-based data)
X_sample = pd.DataFrame(np.random.rand(100, 6), columns=['age', 'bmi', 'blood_pressure', 'cholesterol', 'diabetes', 'smoking'])
y_sample = np.random.randint(0, 2, 100)  # Binary outcome: 1 = High risk, 0 = Low risk

# Model training (using RandomForest for demonstration)
X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict risk level using patient data
input_data = scaler.transform([[patient_data['age'], patient_data['bmi'], patient_data['blood_pressure'],
                                patient_data['cholesterol'], 1 if patient_data['diabetes'] == "Yes" else 0,
                                1 if patient_data['smoking'] == "Current smoker" else 0]])

risk_prediction = model.predict(input_data)[0]
risk_level = "High Risk" if risk_prediction == 1 else "Low Risk"

st.write(f"**Risk Level Prediction:** {risk_level}")

# 3️⃣ Personalized Care Plans
st.header("3. Personalized Care Plans")
st.write("Generate a care plan based on patient risk level, adhering to evidence-based guidelines.")

if risk_level == "High Risk":
    st.write("""
    **Care Plan for High Risk**:
    - **Lifestyle Modifications**: Encourage dietary changes, increased physical activity, and smoking cessation.
    - **Regular Monitoring**: Schedule regular follow-ups to monitor blood pressure, cholesterol, and glucose.
    - **Medication Management**: Ensure adherence to prescribed medications, and adjust as necessary.
    """)
else:
    st.write("""
    **Care Plan for Low Risk**:
    - **Preventive Measures**: Maintain current lifestyle with preventive care practices.
    - **Annual Check-ups**: Schedule yearly assessments for cholesterol, blood pressure, and other metrics.
    - **Self-Monitoring**: Encourage self-monitoring for any new symptoms or lifestyle changes.
    """)

# 4️⃣ Self-Management Support
st.header("4. Self-Management Support")
st.write("Resources and support for managing chronic conditions.")

# Self-management resources
if st.checkbox("Receive Dietary Guidance"):
    st.write("**Resource**: A balanced diet can help reduce cholesterol and manage weight effectively.")
if st.checkbox("Physical Activity Support"):
    st.write("**Resource**: Regular physical activity improves cardiovascular health and reduces risks.")
if st.checkbox("Medication Adherence Assistance"):
    st.write("**Resource**: Consistent medication adherence is crucial for long-term management.")

# 5️⃣ Monitoring & Follow-Up
st.header("5. Monitoring & Follow-Up")
st.write("Track patient progress over time and schedule follow-up appointments based on the care plan.")

follow_up_date = st.date_input("Next Follow-Up Appointment", min_value=datetime.today())
st.write(f"Follow-up scheduled for: {follow_up_date}")

# 6️⃣ Outcome Evaluation
st.header("6. Outcome Evaluation")
st.write("Review outcomes to assess care plan effectiveness and patient progress.")

# Model performance report
y_pred = model.predict(X_test)
st.text("Model Performance Report:")
st.text(classification_report(y_test, y_pred))

# 7️⃣ Quality Improvement
st.header("7. Quality Improvement")
st.write("Use outcome data to enhance chronic care quality over time.")

st.write("""
*Opportunities for Quality Improvement*:
- **Data Analysis**: Regularly analyze patient data to identify trends and areas for improvement.
- **Feedback Mechanism**: Allow patients and providers to give feedback to continuously improve care plans.
- **Updates to Evidence-Based Guidelines**: Integrate new research and guidelines to improve patient outcomes.
""")

# Footer
st.write("Thank you for using our AI-driven, evidence-based chronic care management system!")
