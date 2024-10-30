import streamlit as st
from datetime import datetime

# 1. AI Q&A Section
def get_ai_response(question):
    """
    Function to simulate AI response based on keywords in the question.
    In a real implementation, this would connect to an AI API (e.g., OpenAI GPT).
    """
    question = question.lower()
    
    if "diet" in question or "nutrition" in question:
        answer = (
            "A heart-healthy diet includes fruits, vegetables, whole grains, "
            "lean proteins, and healthy fats. It's essential to limit saturated fats, "
            "trans fats, and sodium."
        )
        references = "Source: American Heart Association"
    
    elif "exercise" in question or "physical activity" in question:
        answer = (
            "Aim for at least 150 minutes of moderate exercise each week, "
            "including both aerobic and strength training activities."
        )
        references = "Source: Centers for Disease Control and Prevention"
    
    elif "medication" in question or "treatment" in question:
        answer = (
            "Always take medications as prescribed by your healthcare provider. "
            "If you have any questions about your treatment plan, consult your provider."
        )
        references = "Source: National Institutes of Health"
    
    elif "hypertension" in question or "blood pressure" in question:
        answer = (
            "To manage hypertension, maintain a low-sodium diet, engage in regular exercise, "
            "and monitor your blood pressure regularly."
        )
        references = "Source: American Heart Association"
    
    elif "diabetes" in question:
        answer = (
            "For diabetes management, monitor your blood sugar levels, maintain a balanced diet, "
            "and adhere to your prescribed medication regimen."
        )
        references = "Source: American Diabetes Association"
    
    elif "copd" in question or "asthma" in question:
        answer = (
            "For COPD and asthma management, avoid triggers, follow your prescribed inhaler regimen, "
            "and participate in pulmonary rehabilitation if recommended."
        )
        references = "Source: American Lung Association"
    
    elif "chronic disease" in question:
        answer = (
            "Managing chronic diseases involves a combination of regular check-ups, medication adherence, "
            "lifestyle modifications, and patient education."
        )
        references = "Source: Centers for Disease Control and Prevention"
    
    else:
        answer = "I'm sorry, but I cannot answer that question at the moment."
        references = "N/A"

    return answer, references

# 2. Patient Input Data Section
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

# 3. AI-Driven Risk Stratification Section
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

# 4. Personalized Care Plans Section
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

# 5. Self-Management Support Section
st.header("4. Self-Management Support")
st.write("Resources and recommendations to help you manage your chronic condition.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Self-Management Step-by-Step Guide**:
    1. **Diet Management**:
        - Plan meals weekly.
        - Keep a food diary to track what you eat.
        - Consult a nutritionist for personalized advice.
    2. **Exercise Routine**:
        - Start with 10-15 minutes of activity daily, gradually increasing.
        - Join a local gym or group exercise class for motivation.
    3. **Medication Management**:
        - Use a pill organizer to track medications.
        - Set reminders on your phone for medication times.
    4. **Health Tracking**:
        - Record daily blood pressure and weight.
        - Use apps to log symptoms and medication adherence.
    5. **Regular Check-Ins**:
        - Schedule weekly check-ins with a healthcare provider or support group.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Self-Management Step-by-Step Guide**:
    1. **Nutrition**:
        - Explore healthy recipes and meal prep options.
        - Consider keeping a food journal for awareness.
    2. **Physical Activity**:
        - Set achievable weekly exercise goals.
        - Incorporate walking or cycling into your daily routine.
    3. **Monitoring Health**:
        - Schedule regular blood pressure and cholesterol checks.
        - Stay informed about your conditions through reliable sources.
    4. **Support Network**:
        - Join community support programs or online groups.
        - Maintain open communication with your healthcare team.
    """)
else:
    st.write("""
    **Low-Risk Self-Management Step-by-Step Guide**:
    1. **Healthy Eating**:
        - Maintain a balanced diet and stay hydrated.
        - Experiment with new healthy recipes.
    2. **Physical Activity**:
        - Engage in activities you enjoy (walking, cycling, swimming).
        - Aim for regular, moderate activity.
    3. **Routine Check-Ups**:
        - Visit your healthcare provider annually for a check-up.
    """)

# 6. Monitoring & Follow-Up Section
st.header("5. Monitoring & Follow-Up")
st.write("Guidelines for monitoring your health based on your risk level.")

if risk_level == "High Risk":
    st.write("""
    **High-Risk Monitoring**:
    - **Blood Pressure**: Weekly checks.
    - **Cholesterol**: Check every 6 months.
    - **Weight**: Weekly weighing.
    - **Follow-Up**: Schedule every 3 months with a healthcare provider.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    **Moderate-Risk Monitoring**:
    - **Blood Pressure**: Weekly checks.
    - **Cholesterol**: Check every 6 months.
    - **Weight**: Weekly weighing.
    - **Follow-Up**: Schedule every 3-6 months with a healthcare provider.
    """)
else:
    st.write("""
    **Low-Risk Monitoring**:
    - **Blood Pressure**: Monthly checks.
    - **Cholesterol**: Check annually.
    - **Weight**: Monthly weighing.
    - **Follow-Up**: Schedule annual check-ups with a healthcare provider.
    """)

# 7. Expected Outcomes Section
st.header("6. Expected Outcomes")
st.write("The expected outcomes of your personalized care plan.")

st.write(f"**Expected Outcomes Based on {risk_level} Status**:")
if risk_level == "High Risk":
    st.write("""
    - **Expected Outcomes**: 
        - Reduced blood pressure and cholesterol levels within 3 months.
        - Improved adherence to medications.
        - Better management of diabetes within 6 months.
    - **Adjustments**: Regularly adjust care plan based on progress.
    """)
elif risk_level == "Moderate Risk":
    st.write("""
    - **Expected Outcomes**: 
        - Stability in health metrics.
        - Improvement in lifestyle habits within 3-6 months.
    - **Adjustments**: Small modifications in diet or activity may be necessary based on outcomes.
    """)
else:
    st.write("""
    - **Expected Outcomes**: 
        - Maintenance of health metrics within a safe range.
        - Prevention of chronic disease onset.
    - **Adjustments**: Continue with current routine; reevaluate annually.
    """)

# 8. Quality Improvement Section
st.header("7. Quality Improvement Insights")
st.write("Our system uses patient outcomes to refine and improve chronic care management.")

st.write("""
For patients classified as high-risk who show no improvement, the AI identifies potential gaps in care strategies.
For patients showing stable or improved results, effective elements of their care plans are highlighted to improve outcomes for other patients.
This feedback loop is key to building an adaptive, evidence-based chronic care system that continually improves based on real-world patient data.
""")

# 9. AI Q&A Section
st.header("8. AI Question and Answer")
st.write("Ask a question related to your health, and our AI will provide evidence-based answers.")

user_question = st.text_input("Type your question here:")
if st.button("Ask"):
    answer, references = get_ai_response(user_question)
    
    st.write(f"**Answer**: {answer}")
    st.write(f"**References**: {references}")

st.write("Thank you for using our AI-driven chronic care management system to support better health outcomes!")
