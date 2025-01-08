import openai

openai.api_key = "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"

async def get_completion():
    completion = await openai.ChatCompletion.create(
        model="gpt-4",  # Correct model name
        messages=[
            { "role": "system", "content": "You are a helpful assistant named Jarvis skilled in general tasks like Alexa and Google Cloud." },
            { "role": "user", "content": "What is coding?" }
        ]
    )
    
    print(completion['choices'][0]['message']['content'])

# Call the function
