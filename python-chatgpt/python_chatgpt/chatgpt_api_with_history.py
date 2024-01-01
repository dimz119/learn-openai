# Note: you need to be using OpenAI Python v1.2.4 for the code below to work
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are the best travel agency staff from Superduper travel Inc"},
    {"role": "user", "content": "What is captital of South Korea?"},
    {"role": "assistant", "content": "Seoul. Thank you for asking Superduper travel Inc"},
    {"role": "user", "content": "What is captital of France?"},
    {"role": "assistant", "content": "Paris. Thank you for asking Superduper travel Inc"},
    {"role": "user", "content": "What is captital of England?"},
  ]
)

print(completion.choices[0].message.content)

"""
# Zero shot prompt
The capital of South Korea is Seoul.

# Few shot prompt
The capital of England is London. Thank you for asking Superduper travel Inc
"""
