# Self-Management Support Section
st.header("4. Self-Management Support")
st.write("Personalized resources and recommendations to help patients self-manage their chronic conditions.")

# AI-driven recommendations based on risk level and care plan
if risk_level == "High Risk":
    st.write("""
    **High-Risk Self-Management Recommendations**:
    - **Diet**: Follow a heart-healthy diet rich in vegetables, whole grains, and lean proteins to manage blood pressure and cholesterol.
    - **Physical Activity**: Aim for at least 150 minutes of moderate-intensity exercise per week, with doctor consultation.
    - **Medication Adherence**: Consistently take medications as prescribed, and consult your doctor if any issues arise.
    - **Mental Health Support**: Consider regular check-ins with a mental health professional for stress management.
    """)
else:
    st.write("""
    **Low-Risk Self-Management Recommendations**:
    - **Diet**: Maintain a balanced diet with portion control to prevent any rise in blood pressure or cholesterol.
    - **Physical Activity**: Aim for moderate physical activity, such as daily walks or light workouts.
    - **Routine Monitoring**: Check blood pressure and cholesterol periodically to ensure they remain in a healthy range.
    - **Preventive Care**: Stay on top of preventive screenings as recommended.
    """)

# Interactive resource checkboxes for further guidance
if st.checkbox("Would you like more dietary guidance?"):
    st.write("A heart-healthy, Mediterranean diet is often recommended for chronic condition management. Visit [MedDiet](https://www.mediterraneandiet.com) for recipes and guidance.")

if st.checkbox("Would you like personalized physical activity support?"):
    st.write("A tailored exercise plan based on your condition can help. Check with your healthcare provider or use an app like MyFitnessPal for tracking activities.")

if st.checkbox("Need help with medication adherence?"):
    st.write("Use tools like mobile reminders or apps (e.g., Medisafe) to improve consistency in taking medications.")

# Monitoring & Follow-Up Section
st.header("5. Monitoring & Follow-Up")
st.write("Track patient progress with AI insights on critical metrics and reminders for follow-up care.")

# AI-Driven Tracking Recommendations based on Risk Level
if risk_level == "High Risk":
    st.write("""
    **High-Risk Monitoring Plan**:
    - **Blood Pressure Monitoring**: Track daily, especially in the morning, and keep a record for healthcare visits.
    - **Cholesterol Monitoring**: Check every 3-6 months, or as directed by your healthcare provider.
    - **Diabetes Monitoring**: If diabetic, measure blood glucose levels daily; consider a continuous glucose monitor if advised.
    - **Follow-Up Frequency**: Schedule follow-ups every 3 months to review and adjust the care plan as needed.
    """)
else:
    st.write("""
    **Low-Risk Monitoring Plan**:
    - **Blood Pressure Monitoring**: Check weekly to ensure levels remain stable.
    - **Cholesterol Monitoring**: Schedule an annual check-up with your healthcare provider.
    - **General Health Check**: Track any changes in symptoms and lifestyle to discuss in your next visit.
    - **Follow-Up Frequency**: Schedule follow-ups once a year unless symptoms or conditions change.
    """)

# Reminder for Follow-Up Appointments
st.date_input("Next Follow-Up Appointment", min_value=datetime.today())

# Outcome Evaluation Section
st.header("6. Outcome Evaluation")
st.write("Evaluate patient outcomes to assess the effectiveness of the care plan.")

# AI Insights Based on Outcome Evaluation
if risk_level == "High Risk":
    st.write("""
    **Outcome Evaluation for High-Risk Patients**:
    - **Expected Outcomes**: Improvement in blood pressure, cholesterol, and overall condition stability.
    - **Adjustment Recommendations**: If no significant improvement is observed, consider modifying the medication dosage, adjusting lifestyle factors, or exploring additional treatment options.
    - **Risk Reduction Insights**: For patients maintaining or improving metrics, we can predict a decrease in long-term complications, enhancing quality of life.
    """)
else:
    st.write("""
    **Outcome Evaluation for Low-Risk Patients**:
    - **Expected Outcomes**: Maintain healthy levels in blood pressure, cholesterol, and other key metrics.
    - **Adjustment Recommendations**: Minor tweaks in diet or activity may be recommended based on yearly outcomes.
    - **Preventive Guidance**: For patients showing stable results, AI suggests ongoing preventive strategies to maintain low-risk status and prevent future escalation.
    """)

# Display a summary based on model prediction and outcome data
st.write("Model Performance for Evaluation:")
st.text(classification_report(y_test, y_pred))

st.write("### Quality Improvement Insights")
st.write("""
Our AI uses outcome data from high-risk patients to guide quality improvement:
- **For non-improving patients**: Identifies trends in care plans that need adjustment.
- **For improving patients**: Highlights effective interventions that can benefit others with similar profiles.
This feedback loop helps refine chronic care practices and improves patient outcomes over time.
""")

st.write("Thank you for using our AI-powered chronic care management system for better health outcomes!")
