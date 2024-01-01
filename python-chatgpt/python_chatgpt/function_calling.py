import json
from openai import OpenAI

client = OpenAI()

def get_current_weather(location: str, unit: str="celsius") -> dict:
    # call weather API
    return {
        "location": location,
        "temperature": 30,
        "unit": unit
    }

def execute_function_call(message):
    if message.tool_calls[0].function.name == "get_current_weather":
        location = json.loads(message.tool_calls[0].function.arguments)["location"]
        results = get_current_weather(location, 'celsius')
    else:
        results = f"Error: function {message.tool_calls[0].function.name} does not exist"
    return results

tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]
messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

# https://platform.openai.com/docs/api-reference/chat
"""
ChatCompletion(
    id='chatcmpl-8c4kkiTYPQbeOL8HmjhIIMotB7BL3',
    choices=[
        Choice(
            finish_reason='tool_calls',
            index=0,
            logprobs=None,
            message=ChatCompletionMessage(
                content=None,
                role='assistant',
                function_call=None,
                tool_calls=[
                    ChatCompletionMessageToolCall(
                        id='call_SnEXXv3Oa6eTsDVKNCYcmkql',
                        function=Function(
                            arguments='{\n"location": "Boston, MA"\n}',
                            name='get_current_weather'),
                            type='function'
                        )
                ]
            )
        )
    ],
    created=1704085426,
    model='gpt-3.5-turbo-0613',
    object='chat.completion',
    system_fingerprint=None,
    usage=CompletionUsage(completion_tokens=17, prompt_tokens=83, total_tokens=100))
"""

assistant_message = completion.choices[0].message

if assistant_message.tool_calls[0]:
    result = execute_function_call(assistant_message)
    print(f"The weather in {result['location']} is {result['temperature']} {result['unit']}")
    """
    The weather in Boston, MA is 15 celsius
    """

