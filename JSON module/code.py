import json

# 1. to convert a JSON string to a Python dictionary, we can use the json.loads() method.

str_json = '{"name": "John Doe", "age": 30, "email": "kashif@example.com", "isTrue":true}'
# data = json.loads(str_json)
# print(type(data), data) 

# with open('data.json','r') as f:
#     data = json.load(f)
#     print(type(data), data)





# 2. to convert a Python dictionary to a JSON string, we can use the json.dumps() method.

str_python = {
    "name": "John Doe",
    "age": 30,
    "isTrue": True
}

data = json.dumps(str_python)
print(type(data), data)