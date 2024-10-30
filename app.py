import streamlit as st
import openai

# Initialize OpenAI API Key
openai.api_key = "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"

# Function to get AI response using OpenAI
def get_ai_response(question):
    try:
        # Query the OpenAI API using the new method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this model is available for your key
            messages=[
                {"role": "user", "content": question}
            ]
        )
        # Extracting the answer
        answer = response['choices'][0]['message']['content']
        return answer, "Source: OpenAI"
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log error to console for debugging
        return f"I'm sorry, but I cannot answer that question at the moment. Error: {str(e)}", "N/A"

# Streamlit UI
st.title("Chronic Care Management System")
st.header("AI Question and Answer")
st.write("Ask a question related to your health, and our AI will provide evidence-based answers.")

user_question = st.text_input("Type your question here:")

if st.button("Ask"):
    if user_question.strip():  # Check for non-empty input
        answer, references = get_ai_response(user_question)
        st.write(f"**Answer**: {answer}")
        st.write(f"**References**: {references}")
    else:
        st.write("Please enter a question before clicking 'Ask'.")

st.write("Thank you for using our AI-driven chronic care management system!")
