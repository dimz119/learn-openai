# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# compared to "response = openai.Completion.create( ... ) before "
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message'])
