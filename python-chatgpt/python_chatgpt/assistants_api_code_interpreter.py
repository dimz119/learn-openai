import time
from openai import OpenAI

# make sure you have OPENAI_API_KEY environment variable with API key
# export OPENAI_API_KEY=""

client = OpenAI()

# upload the reference file
file = client.files.create(
            file=open("sample/fortune_1000_revenue_2022.csv", "rb"),
            purpose='assistants')

print(file.id)

# create assistant
assistant = client.beta.assistants.create(
                instructions="You are very good at creating plot given csv file. Use your knowledge base from csv file to best respond to customer queries.",
                model="gpt-4-1106-preview",
                tools=[
                    {"type": "code_interpreter"},
                    {"type": "retrieval"}
                ],
                file_ids=[file.id])

# create a thread
thread = client.beta.threads.create()

# create a message with file.id in the thread
message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="Create a plot based on top 10 of 2022 fortune 1000 companies revenue",
            file_ids=[file.id])

# run with the specific instruction
run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions=f"Use the file {file.id} if it is necessary")

while True:
    run_resp = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    if run_resp.status == 'completed':
        break
    print(f"Waiting ... {run_resp.status}")
    time.sleep(3)

messages = client.beta.threads.messages.list(
                thread_id=thread.id,
                order="asc",
                after=message.id)

for thread_message in messages.data:
    print(thread_message)

"""
ThreadMessage(id='msg_1RGEyl4a6j4JOJ6sBXdA4wjd', assistant_id='asst_XEq150Oj93VJdBs8qy8xzLz9', content=[
    MessageContentText(text=Text(annotations=[], 
        value="Since the file is not accessible with the `myfiles_browser` tool, 
                I will proceed by inspecting the content of the file and extracting the necessary information 
                to create the plot. Let's start by opening the file to see its content."), type='text')], created_at=1704521040, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_SQ2AAMc3801mDYVVckxv3QpO', thread_id='thread_gwbTw6aQ1FZ1gFvg1gm5y3tQ')

ThreadMessage(id='msg_tBfVr0NBTGSUDpSF8BM4Jagl', assistant_id='asst_XEq150Oj93VJdBs8qy8xzLz9', content=[
    MessageContentText(text=Text(annotations=[], 
        value="The file appears to be a CSV-formatted text containing the ranking data for the Fortune 1000 companies, 
                specifically showing the top companies by revenue for the year 2022. 
                The first line of the content is the header, and it indicates the fields in the CSV 
                (rank, name, revenues, etc.).\n\n
                Let's proceed by loading the entire content into a DataFrame and then we will visualize the top 10 companies by revenue."), type='text')], created_at=1704521053, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_SQ2AAMc3801mDYVVckxv3QpO', thread_id='thread_gwbTw6aQ1FZ1gFvg1gm5y3tQ')

ThreadMessage(id='msg_bF4SB3TZJKNXjWoBlf0tc2l8', assistant_id='asst_XEq150Oj93VJdBs8qy8xzLz9', content=[
    MessageContentText(text=Text(annotations=[], 
        value="The DataFrame has been loaded successfully. We have the top 5 companies by revenue listed, although we need the top 10 for the plot. 
        The `revenues` column figures are formatted as strings with dollar signs and commas, so we'll need to clean that up and convert to numeric values 
        for plotting.\n\nNow, I'll extract the top 10 companies by revenue and create a bar plot to visualize their revenues."), type='text')], created_at=1704521066, file_ids=[], metadata={}, object='thread.message', role='assistant', run_id='run_SQ2AAMc3801mDYVVckxv3QpO', thread_id='thread_gwbTw6aQ1FZ1gFvg1gm5y3tQ')

ThreadMessage(id='msg_Dtvrn6REt99Y0W9VWEl0y43l', assistant_id='asst_XEq150Oj93VJdBs8qy8xzLz9', content=[
    MessageContentImageFile(image_file=ImageFile(
        file_id='file-X12KV89P9Kl2KBy2QVw2mEM6'), type='image_file'), MessageContentText(text=Text(annotations=[TextAnnotationFilePath(end_index=336, file_path=TextAnnotationFilePathFilePath(file_id='file-xsoWTOwfKC8tioOax2nQpEME'), start_index=272, text='sandbox:/mnt/data/top_10_fortune_1000_companies_revenue_2022.png', type='file_path')], value='The bar plot visualizes the revenues of the top 10 companies from the 2022 Fortune 1000 list. The company with the highest revenue, Walmart, is shown at the top of the plot, with the other companies listed in descending order of revenue.\n\nYou can download the plot [here](sandbox:/mnt/data/top_10_fortune_1000_companies_revenue_2022.png).'), type='text')], created_at=1704521089, file_ids=['file-xsoWTOwfKC8tioOax2nQpEME'], metadata={}, object='thread.message', role='assistant', run_id='run_SQ2AAMc3801mDYVVckxv3QpO', thread_id='thread_gwbTw6aQ1FZ1gFvg1gm5y3tQ')
"""

# retrieve the file and write the file in byte
image = client.files.content('file-X12KV89P9Kl2KBy2QVw2mEM6') # type file id from your result
with open('plot.png', 'wb') as file:
    file.write(image.content)
