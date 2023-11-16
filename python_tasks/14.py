import json

def mean_age(json_string):
    json_list = json.loads(json_string)
    age_list = [i.get("age") for i in json_list]
    return json.dumps({"mean_age": sum(age_list)/len(age_list)})