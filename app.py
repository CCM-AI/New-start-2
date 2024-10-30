import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Title for the app
st.title("Chronic Care Management System")

# 1️⃣ **Patient Input Data**
st.header("1. Patient Input Data")
st.write("Enter patient details for chronic care management.")

# Sample patient data input form
patient_data = {
    "age": st.number_input("Age", min_value=0, max_value=120, value=30),
    "weight": st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0),
    "height": st.number_input("Height (cm)", min_value=0, max_value=250, value=170),
    "blood_pressure": st.slider("Blood Pressure (mm Hg)", 80, 200, 120),
    "cholesterol": st.slider("Cholesterol Level (mg/dL)", 100, 300, 180),
    "diabetes": st.selectbox("Diabetes Status", ["No", "Yes"]),
}

# **Submit Patient Data**
if st.button("Submit Patient Data"):
    st.success("Patient data submitted successfully!")

# 2️⃣ **AI-Driven Risk Stratification**
st.header("2. AI-Driven Risk Stratification")
st.write("The system will assess the patient's risk level based on input data.")

# Sample data for model training
X = pd.DataFrame(np.random.rand(100, 4), columns=['age', 'weight', 'height', 'blood_pressure'])
y = np.random.randint(0, 2, 100)  # Random binary outcome

# Simple logistic regression model for demonstration
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict risk level (this would normally use the actual patient data)
risk_prediction = model.predict([[patient_data['age'], patient_data['weight'], patient_data['height'], patient_data['blood_pressure']]])[0]
risk_level = "High Risk" if risk_prediction == 1 else "Low Risk"

st.write(f"**Risk Level:** {risk_level}")

# 3️⃣ **Personalized Care Plans**
st.header("3. Personalized Care Plans")
st.write("Based on risk level, a personalized care plan is recommended.")

if risk_level == "High Risk":
    st.write("Recommended care plan: Increased monitoring and lifestyle adjustments.")
else:
    st.write("Recommended care plan: Regular monitoring and preventive care.")

# 4️⃣ **Self-Management Support**
st.header("4. Self-Management Support")
st.write("Provide resources and support for patients to self-manage their chronic condition.")

# Self-management options
st.checkbox("Dietary Counseling")
st.checkbox("Physical Activity Support")
st.checkbox("Medication Adherence Assistance")

# 5️⃣ **Monitoring & Follow-Up**
st.header("5. Monitoring & Follow-Up")
st.write("Track patient progress over time and schedule follow-up appointments.")

# 6️⃣ **Outcome Evaluation**
st.header("6. Outcome Evaluation")
st.write("Evaluate outcomes to determine the effectiveness of the care plan.")

# Simulated model outcome evaluation
y_pred = model.predict(X_test)
st.text(classification_report(y_test, y_pred))

# 7️⃣ **Quality Improvement**
st.header("7. Quality Improvement")
st.write("Use the outcome data to identify opportunities for quality improvement.")
st.write("Analyze trends, adjust care plans, and enhance chronic care management.")

# End of app
st.write("Thank you for using the Chronic Care Management System!")
