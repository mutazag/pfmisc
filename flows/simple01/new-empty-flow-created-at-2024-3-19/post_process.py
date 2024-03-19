
from promptflow import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def post_process(input1: str) -> str:
    try:
        return json.loads(input1)
    except Exception as e:
        print(f'Input is not valid, error: {e}')
        return {"category": "None", "evidence" : "None}"}
