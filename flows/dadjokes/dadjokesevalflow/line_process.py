from promptflow import tool


@tool
def line_process(jokescore: str):
    import json

    jokescore_json = json.loads(jokescore)
    jokescore_dict = dict(jokescore_json)

    load_list = [
        {"name": "comedic_value", "score": jokescore_dict['comedic_value']}, 
        {"name": "comedic_relevance", "score": jokescore_dict['comedic_relevance']}
    ]


    variant_level_result = {}
    for item in load_list:
        item_name = str(item["name"])
        variant_level_result[item_name] = item["score"]
        variant_level_result[item_name + '_pass_rate'] = 1 if item["score"] > 3 else 0
    return variant_level_result
    # return jokescore_dict
