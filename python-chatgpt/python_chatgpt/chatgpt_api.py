# Note: you need to be using OpenAI Python v1.2.4 for the code below to work
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)

# # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# # compared to "response = openai.Completion.create( ... ) before "
# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

# print(response['choices'][0]['message'])
