import openai

openai.api_key = "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"

question = "What are the symptoms of diabetes?"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    answer = response.choices[0].message['content']
    print(f"Answer: {answer}")
except Exception as e:
    print(f"Error: {str(e)}")
