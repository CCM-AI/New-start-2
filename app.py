# Import required libraries
import streamlit as st
from datetime import datetime
from sklearn.metrics import classification_report
import numpy as np

# 1. Patient Input Data Section
st.header("1. Patient Input Data")
st.write("Please fill in your details to help us assess your chronic care needs.")

age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0)
cholesterol_level = st.number_input("Cholesterol Level (mg/dL)", min_value=0)
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
smoking_status = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
physical_activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])

# Collect data in a dictionary for AI processing
patient_data = {
    "age": age,
    "gender": gender,
    "blood_pressure": blood_pressure,
    "cholesterol_level": cholesterol_level,
    "diabetes": diabetes,
    "smoking_status": smoking_status,
    "physical_activity": physical_activity
}

# 2. AI-Driven Risk Stratification Section
st.header("2. AI-Driven Risk Stratification")
st.write("Our AI will assess your risk level based on your input data.")

# Simplified risk model based on input data
if blood_pressure > 140 or cholesterol_level > 240 or diabetes == "Yes":
    risk_level = "High Risk"
elif age > 50 or smoking_status == "Current" or physical_activity == "Low":
    risk_level = "Moderate Risk"
else:
    risk_level = "Low Risk"

st.write(f"**Your Risk Level**: {risk_level}")

# 3. Personalized Care Plans Section
st.header("3. Personalized Care Plans")
st.write("Your customized care plan based on the AI-driven risk assessment.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Care Plan**:
    - **Diet**: Focus on heart-healthy foods and limit salt intake.
    - **Exercise**: Aim for moderate exercise, like brisk walking, for 150 minutes per week.
    - **Regular Monitoring**: Check blood pressure and cholesterol frequently.
    - **Medication Adherence**: Follow up with your healthcare provider for medication adherence.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Care Plan**:
    - **Diet**: Adopt a balanced diet with a variety of foods.
    - **Exercise**: Stay active, targeting 150 minutes per week of physical activity.
    - **Monitoring**: Regularly check your blood pressure and cholesterol.
    - **Preventive Measures**: Stay up-to-date with screenings and check-ups.
    """)
else:
    st.write("""
    **Low-Risk Care Plan**:
    - **Diet**: Continue with a balanced diet to maintain current health.
    - **Exercise**: Keep up with moderate physical activity.
    - **Annual Monitoring**: Routine annual check-up to monitor key metrics.
    """)

# 4. Self-Management Support Section
st.header("4. Self-Management Support")
st.write("Resources and recommendations to help you manage your chronic condition.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Self-Management Tips**:
    - **Diet**: Follow a Mediterranean or DASH diet.
    - **Exercise**: Include both cardio and strength exercises with your doctor's guidance.
    - **Medication Management**: Use reminders or apps to adhere to medication.
    - **Mental Health**: Consider regular check-ins with a counselor.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Self-Management Tips**:
    - **Diet**: Maintain a diet rich in fruits, vegetables, and lean proteins.
    - **Physical Activity**: Aim for 150 minutes of weekly exercise.
    - **Routine Monitoring**: Track blood pressure and cholesterol as advised.
    """)
else:
    st.write("""
    **Low-Risk Self-Management Tips**:
    - **Diet**: Continue with a balanced, portion-controlled diet.
    - **Exercise**: Engage in regular activities like walking, biking, or swimming.
    - **Preventive Screenings**: Maintain routine health screenings.
    """)

# 5. Monitoring & Follow-Up Section
st.header("5. Monitoring & Follow-Up")
st.write("Ongoing tracking and follow-up to ensure optimal care.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Monitoring**:
    - **Blood Pressure**: Check daily or as advised by your healthcare provider.
    - **Cholesterol and Diabetes**: Test every 3-6 months.
    - **Follow-Up**: Schedule check-ups every 3 months.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Monitoring**:
    - **Blood Pressure**: Check weekly.
    - **Cholesterol**: Monitor every 6-12 months.
    - **Follow-Up**: Schedule annual or bi-annual check-ups.
    """)
else:
    st.write("""
    **Low-Risk Monitoring**:
    - **Blood Pressure**: Monitor as advised, typically yearly.
    - **Cholesterol**: Check yearly.
    - **Follow-Up**: Routine annual check-ups.
    """)

# 6. Outcome Evaluation Section
st.header("6. Outcome Evaluation")
st.write("Evaluating outcomes based on your progress and AI insights.")

# Placeholder model data - replace with actual model outcome if available
y_test = np.array([0, 1, 1, 0])  # Example true labels
y_pred = np.array([0, 1, 0, 0])  # Example predicted labels

try:
    st.write("Model Evaluation Report:")
    st.text(classification_report(y_test, y_pred))
except Exception as e:
    st.error(f"Model evaluation error: {e}")

st.write(f"**Outcome Evaluation Based on {risk_level} Status**:")
if risk_level == "High Risk":
    st.write("""
    - **Expected Outcomes**: Reduced blood pressure and cholesterol, improved medication adherence.
    - **Adjustments**: Modify medication or increase activity levels if no improvement.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    - **Expected Outcomes**: Stability in health metrics.
    - **Adjustments**: Small adjustments in diet or activity if results aren’t optimal.
    """)
else:
    st.write("""
    - **Expected Outcomes**: Maintenance of health metrics in a safe range.
    - **Adjustments**: Continue current routine unless metrics change.
    """)

# 7. Quality Improvement Section
st.header("7. Quality Improvement Insights")
st.write("Our system uses patient outcomes to refine and improve chronic care management.")

st.write("""
For patients classified as high-risk who show no improvement, the AI identifies potential gaps in care strategies.
For patients showing stable or improved results, effective elements of their care plans are highlighted to improve outcomes for other patients.
This feedback loop is key to building an adaptive, evidence-based chronic care system that continually improves based on real-world patient data.
""")

st.write("Thank you for using our AI-driven chronic care management system to support better health outcomes!")
