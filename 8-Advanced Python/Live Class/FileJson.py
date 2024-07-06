import json

fileName = "exJson.json"

with open(fileName, "rt") as fp:
    data = json.loads(fp.read())
    print(data)
    print(type(data))

    for k, v in data.items():
        print(k, v)
