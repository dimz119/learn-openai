# Note: you need to be using OpenAI Python v1.2.4 for the code below to work
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

history_message = [
    {"role": "system", "content": "You are the best travel agency staff from Superduper travel Inc"},
    {"role": "user", "content": "What is captital of South Korea?"},
    {"role": "assistant", "content": "Seoul. Thank you for asking Superduper travel Inc"},
    {"role": "user", "content": "What is captital of France?"},
    {"role": "assistant", "content": "Paris. Thank you for asking Superduper travel Inc"}
]

end_word = 'quit'
print(f"Thank you for visiting Superduper travel Inc. To end the chat, type {end_word}\n\n")
user_question = ""

while True:
    user_question = input("Any question? ")

    if user_question == end_word:
        print(f"Thank you for reaching out to Superduper travel Inc, Bye now!")
        break

    history_message.append({
        "role": "user",
        "content": user_question})

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=history_message
    )

    response = completion.choices[0].message.content
    print(response)

    history_message.append({
      "role": "assistant",
      "content": response})

    print("\n\n")
