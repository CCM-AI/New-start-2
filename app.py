import streamlit as st
from datetime import datetime
import openai

# Initialize OpenAI API Key
openai.api_key = "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"

# Function to get AI response using OpenAI with updated API
def get_ai_response(question):
    try:
        # Query the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated model name, you can use "gpt-4" if available
            messages=[
                {"role": "user", "content": question}
            ]
        )
        # Extracting the answer
        answer = response.choices[0].message['content']
        return answer, "Source: OpenAI"
    except Exception as e:
        return f"An error occurred: {e}", "N/A"

# Streamlit app layout
st.header("1. Patient Input Data")
st.write("Please fill in your details to help us assess your chronic care needs.")

# Patient Demographics
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Cardiovascular Disease Risk Assessment
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0)
cholesterol_level = st.number_input("Cholesterol Level (mg/dL)", min_value=0)
heart_disease_family_history = st.selectbox("Family History of Heart Disease", ["Yes", "No"])
smoking_status = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
physical_activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])

# Hypertension Risk Assessment
hypertension_history = st.selectbox("History of Hypertension", ["Yes", "No"])
hypertension_treatment = st.selectbox("Currently Under Treatment for Hypertension", ["Yes", "No"])

# Diabetes Assessment
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
diabetes_treatment = st.selectbox("Currently Under Treatment for Diabetes", ["Yes", "No"])

# COPD and Asthma Assessment
copd = st.selectbox("Chronic Obstructive Pulmonary Disease (COPD)", ["Yes", "No"])
asthma = st.selectbox("Asthma", ["Yes", "No"])

# Collect data in a dictionary for AI processing
patient_data = {
    "age": age,
    "gender": gender,
    "blood_pressure": blood_pressure,
    "cholesterol_level": cholesterol_level,
    "heart_disease_family_history": heart_disease_family_history,
    "smoking_status": smoking_status,
    "physical_activity": physical_activity,
    "hypertension_history": hypertension_history,
    "hypertension_treatment": hypertension_treatment,
    "diabetes": diabetes,
    "diabetes_treatment": diabetes_treatment,
    "copd": copd,
    "asthma": asthma,
}

# 2. AI-Driven Risk Stratification Section
st.header("2. AI-Driven Risk Stratification")
st.write("Our AI will assess your risk level based on your input data.")

# Simplified risk model based on input data
risk_level = "Low Risk"
risk_explanation = ""

if blood_pressure > 140 or cholesterol_level > 240 or diabetes == "Yes":
    risk_level = "High Risk"
    risk_explanation = "You are at high risk due to poor control of blood pressure, cholesterol, or existing diabetes."
elif age > 50 or smoking_status == "Current" or physical_activity == "Low" or hypertension_history == "Yes":
    risk_level = "Moderate Risk"
    risk_explanation = "You are at moderate risk due to your age, smoking status, or a history of hypertension."
elif age < 50 and smoking_status == "Never" and physical_activity == "High":
    risk_level = "Low Risk"
    risk_explanation = "You have a low risk level based on your age, lifestyle, and absence of major risk factors."

st.write(f"**Your Risk Level**: {risk_level}")
st.write(f"**Explanation**: {risk_explanation}")

# 3. Personalized Care Plans Section
st.header("3. Personalized Care Plans")
st.write("Your customized care plan based on the AI-driven risk assessment.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Care Plan**:
    - **Diet**: Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins. Limit saturated fats and sodium.
    - **Exercise**: Engage in at least 150 minutes of moderate aerobic exercise each week. Include strength training twice weekly.
    - **Regular Monitoring**: Check blood pressure and cholesterol levels monthly.
    - **Medication Adherence**: Take prescribed medications consistently. Schedule regular reviews with your healthcare provider.
    - **Mental Health**: Consider counseling or support groups for emotional support.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Care Plan**:
    - **Diet**: Follow a balanced diet that includes a variety of nutrients. Monitor portion sizes and limit processed foods.
    - **Exercise**: Aim for at least 150 minutes of moderate exercise weekly; incorporate strength training sessions.
    - **Monitoring**: Check blood pressure and cholesterol every 6 months.
    - **Preventive Measures**: Stay up-to-date with screenings and health checks.
    - **Mental Health**: Maintain social connections and consider mindfulness practices.
    """)
else:
    st.write("""
    **Low-Risk Care Plan**:
    - **Diet**: Continue a healthy, balanced diet. Focus on whole foods and hydration.
    - **Exercise**: Maintain regular physical activity; aim for 150 minutes per week.
    - **Annual Monitoring**: Routine annual check-up for blood pressure and cholesterol.
    - **Preventive Screenings**: Keep up with preventive screenings based on age and gender.
    """)

# AI Question and Answer Section
st.header("8. AI Question and Answer")
st.write("Ask a question related to your health, and our AI will provide evidence-based answers.")

user_question = st.text_input("Type your question here:")
if st.button("Ask"):
    answer, references = get_ai_response(user_question)
    
    st.write(f"**Answer**: {answer}")
    st.write(f"**References**: {references}")

st.write("Thank you for using our AI-driven chronic care management system to support better health outcomes!")
