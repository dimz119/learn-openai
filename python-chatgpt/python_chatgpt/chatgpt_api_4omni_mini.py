# Note: you need to be using OpenAI Python v1.2.4 for the code below to work
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)
