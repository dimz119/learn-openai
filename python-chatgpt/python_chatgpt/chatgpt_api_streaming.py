# Note: you need to be using OpenAI Python v1.2.4 for the code below to work
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content)


# # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# import openai
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# for chunk in openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": "Generate a list of 100 best travel recommendable cities"}
#     ],
#     stream=True,
# ):
#     content = chunk["choices"][0].get("delta", {}).get("content")
#     if content is not None:
#         print(content, end='')
