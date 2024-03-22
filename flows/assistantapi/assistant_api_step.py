
from promptflow import tool
from promptflow.connections import AzureOpenAIConnection 
from promptflow.contracts.types import PromptTemplate
from openai import AzureOpenAI
from jinja2 import Template
import time


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(

    input1: str, 
    aoaiconn : AzureOpenAIConnection, 
    deployment_name: str = "gpt-4-default-aueast",
    ) -> str:

    print(aoaiconn.api_base)

    print(aoaiconn.api_key)

    # rendered_prompt = Template(prompt, trim_blocks=True, keep_trailing_newline=True).render(**kwargs)


    client = AzureOpenAI(
        api_key= aoaiconn.api_key, #os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-02-15-preview",
        azure_endpoint=aoaiconn.api_base # os.getenv("AZURE_OPENAI_ENDPOINT")
        )


    # Create an assistant
    assistant = client.beta.assistants.create(
        name="Math Assist",
        instructions=input1,
        tools=[{"type": "code_interpreter"}],
        model=deployment_name
    )



    # add a file to assistant 
    # client.beta.assistants.files.create(
    #     assistant.id, 

    # )

    # Create a thread
    thread = client.beta.threads.create()

    # Add a user question to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )

    # Run the thread
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Retrieve the status of the run
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    status = run.status

    # Wait till the assistant has responded
    while status not in ["completed", "cancelled", "expired", "failed"]:
        time.sleep(5)
        run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
        status = run.status

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )


# Prints the messages with the latest message at the bottom
    number_of_messages = len(messages.data)
    print( f'Number of messages: {number_of_messages}')

    assistant_response = ''
    for message in reversed(messages.data):
        role = message.role  
        for content in message.content:
            if content.type == 'text':
                response = content.text.value 
                print(f'\n{role}: {response}')
                if role == 'assistant':
                    assistant_response = response  
    
    return assistant_response
