from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

# create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)
print(assistant.id)
"""
asst_xRWVlhCHd6d20sQPIZulQ4dC
"""

# create a thread. This will have unlimited messages, but won't be used all
thread = client.beta.threads.create()
print(thread.id)
"""
thread_B1vjbdanR7ljZA8xoBcOnZDe
"""

# create a message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

print(run.status)
"""
queued
"""

print(run.id)
"""
run_s4GaPrJ75jfxpOYeCSnFpPzE
"""

run = client.beta.threads.runs.retrieve(
    thread_id="thread_B1vjbdanR7ljZA8xoBcOnZDe",
    run_id="run_s4GaPrJ75jfxpOYeCSnFpPzE"
)

print(run.status)
"""
completed
"""

# run = client.beta.threads.runs.retrieve(
#   thread_id=thread.id,
#   run_id=run.id
# )

messages = client.beta.threads.messages.list(
    thread_id="thread_B1vjbdanR7ljZA8xoBcOnZDe"
)

print(messages)
"""
SyncCursorPage[ThreadMessage](
    data=[
        ThreadMessage(
            id='msg_sZFHn3QO0W5vffw8ag4lM1X3', 
            assistant_id='asst_xRWVlhCHd6d20sQPIZulQ4dC',
            content=[MessageContentText(
                text=Text(
                    annotations=[],
                    value='The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\).'),
                    type='text')
            ],
            created_at=1704155558,
            file_ids=[],
            metadata={},
            object='thread.message',
            role='assistant',
            run_id='run_s4GaPrJ75jfxpOYeCSnFpPzE',
            thread_id='thread_B1vjbdanR7ljZA8xoBcOnZDe'), 
        ThreadMessage(
            id='msg_AXT7R03S28JPzu2QPfT8BRoV',
            assistant_id=None,
            content=[MessageContentText(
                text=Text(
                    annotations=[],
                    value='I need to solve the equation `3x + 11 = 14`. Can you help me?'),
                    type='text')
            ],
            created_at=1704155546,
            file_ids=[],
            metadata={},
            object='thread.message',
            role='user',
            run_id=None,
            thread_id='thread_B1vjbdanR7ljZA8xoBcOnZDe')
    ],
    object='list',
    first_id='msg_sZFHn3QO0W5vffw8ag4lM1X3'.
    last_id='msg_AXT7R03S28JPzu2QPfT8BRoV',
    has_more=False)
"""

for thread_message in messages.data:
    print(thread_message.content[0].text.value)
"""
The solution to the equation \(3x + 11 = 14\) is \(x = 1\).
I need to solve the equation `3x + 11 = 14`. Can you help me?
"""

run_steps = client.beta.threads.runs.steps.list(
    thread_id="thread_B1vjbdanR7ljZA8xoBcOnZDe",
    run_id="run_s4GaPrJ75jfxpOYeCSnFpPzE"
)

print(run_steps)
"""
SyncCursorPage[RunStep](
    data=[
        RunStep(
            id='step_sR9CfL9847GRq72CTqTK7P0m',
            assistant_id='asst_xRWVlhCHd6d20sQPIZulQ4dC',
            cancelled_at=None,
            completed_at=1704155559,
            created_at=1704155558,
            expired_at=None,
            failed_at=None,
            last_error=None,
            metadata=None,
            object='thread.run.step',
            run_id='run_s4GaPrJ75jfxpOYeCSnFpPzE',
            status='completed',
            step_details=MessageCreationStepDetails(
                message_creation=MessageCreation(
                    message_id='msg_sZFHn3QO0W5vffw8ag4lM1X3'),
                type='message_creation'
            ),
            thread_id='thread_B1vjbdanR7ljZA8xoBcOnZDe',
            type='message_creation',
            expires_at=None),

        RunStep(
            id='step_XusmCVYC8m3AXYJuVaVSOwVo',
            assistant_id='asst_xRWVlhCHd6d20sQPIZulQ4dC',
            cancelled_at=None,
            completed_at=1704155558,
            created_at=1704155548,
            expired_at=None,
            failed_at=None,
            last_error=None,
            metadata=None,
            object='thread.run.step',
            run_id='run_s4GaPrJ75jfxpOYeCSnFpPzE',
            status='completed',
            step_details=ToolCallsStepDetails(
                tool_calls=[
                    CodeToolCall(
                        id='call_ZUnZKdhjd2s8NxodspmMyLHh',
                        code_interpreter=CodeInterpreter(
                            input="
                                
                                from sympy import symbols, Eq, solve

                                # Define the symbol
                                x = symbols('x')

                                # Define the equation
                                equation = Eq(3*x + 11, 14)

                                # Solve the equation
                                solution = solve(equation, x)
                                solution
                                
                                ",
                            outputs=[
                                CodeInterpreterOutputLogs(
                                    logs='[1]',
                                    type='logs')
                                ]
                        ), 
                        type='code_interpreter'
                    )
                ],
                type='tool_calls'
            ),
            thread_id='thread_B1vjbdanR7ljZA8xoBcOnZDe',
            type='tool_calls',
            expires_at=None
        )
    ],
    object='list',
    first_id='step_sR9CfL9847GRq72CTqTK7P0m',
    last_id='step_XusmCVYC8m3AXYJuVaVSOwVo',
    has_more=False)
"""

assistant_list = client.beta.assistants.list(order="desc", limit=5)
print(assistant_list.data)
"""
[
    Assistant(id='asst_xRWVlhCHd6d20sQPIZulQ4dC', created_at=1704155546, description=None, file_ids=[], instructions='You are a personal math tutor. Write and run code to answer math questions.', metadata={}, model='gpt-4-1106-preview', name='Math Tutor', object='assistant', tools=[ToolCodeInterpreter(type='code_interpreter')]),
    Assistant(id='asst_DM5d6fTSX67ZcC4GS5GzBY2y', created_at=1704155508, description=None, file_ids=[], instructions='You are a personal math tutor. Write and run code to answer math questions.', metadata={}, model='gpt-4-1106-preview', name='Math Tutor', object='assistant', tools=[ToolCodeInterpreter(type='code_interpreter')])]
"""

# delete the assistant
print(client.beta.assistants.delete("asst_DM5d6fTSX67ZcC4GS5GzBY2y"))
