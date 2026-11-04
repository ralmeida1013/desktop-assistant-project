import ollama

print("Asking the AI brain...")
response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': 'Introduce yourself as a local desktop assistant named J.A.R.V.I.S. in one short sentence.',
    },
])

print("\nAI Response:")
print(response['message']['content'])
