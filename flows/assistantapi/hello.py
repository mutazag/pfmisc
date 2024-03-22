# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
from openai import AzureOpenAI

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def my_python_tool(input1: str, aoaiconn : AzureOpenAIConnection) -> str:

        
    client = AzureOpenAI(
        api_key= aoaiconn.api_key, #os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-02-15-preview",
        azure_endpoint=aoaiconn.base_url # os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    # # Create an assistant
    # assistant = client.beta.assistants.create(
    #     name="Math Assist",
    #     instructions="You are an AI assistant that can write code to help answer math questions.",
    #     tools=[{"type": "code_interpreter"}],
    #     model="gpt-4-1106-preview" #You must replace this value with the deployment name for your model.
    # )

    # # Create a thread
    # thread = client.beta.threads.create()

    # # Add a user question to the thread
    # message = client.beta.threads.messages.create(
    #     thread_id=thread.id,
    #     role="user",
    #     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    # )

    # # Run the thread
    # run = client.beta.threads.runs.create(
    # thread_id=thread.id,
    # assistant_id=assistant.id,
    # )

    # # Retrieve the status of the run
    # run = client.beta.threads.runs.retrieve(
    # thread_id=thread.id,
    # run_id=run.id
    # )

    # status = run.status

    # # Wait till the assistant has responded
    # while status not in ["completed", "cancelled", "expired", "failed"]:
    #     time.sleep(5)
    #     run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    #     status = run.status

    # messages = client.beta.threads.messages.list(
    # thread_id=thread.id
    # )

    # print(messages.model_dump_json(indent=2))



    return "Prompt: " + input1



