from pydantic import BaseModel

from openai import OpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: list[Step]
    final_answer: str


client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "solve 8x + 31 = 2"},
    ],
    response_format=MathResponse,
)

message = completion.choices[0].message
if message.parsed:
    print(message.parsed.steps)
    print(message.parsed.final_answer)
else:
    print(message.refusal)
""" Output
[Step(explanation='Subtract 31 from both sides of the equation to start isolating x on one side.', output='8x + 31 - 31 = 2 - 31'), Step(explanation='Simplify both sides. On the left side, 31 - 31 is 0, and on the right side, 2 - 31 is -29.', output='8x = -29'), Step(explanation='Divide both sides by 8 to solve for x.', output='x = -29 / 8')]
x = -29/8
"""
