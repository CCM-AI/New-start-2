import streamlit as st
import openai

# Initialize OpenAI API Key
openai.api_key = "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"

# Function to get AI response using OpenAI
def get_ai_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message['content']
        return answer, "Source: OpenAI"
    except Exception as e:
        return "I'm sorry, but I cannot answer that question at the moment.", "N/A"

# Streamlit UI
st.title("Chronic Care Management System")
st.header("AI Question and Answer")
st.write("Ask a question related to your health, and our AI will provide evidence-based answers.")

user_question = st.text_input("Type your question here:")
if st.button("Ask"):
    if user_question:
        answer, references = get_ai_response(user_question)
        st.write(f"**Answer**: {answer}")
        st.write(f"**References**: {references}")
    else:
        st.write("Please enter a question before clicking 'Ask'.")

st.write("Thank you for using our AI-driven chronic care management system!")
