import json
with open('data.txt') as json_data:
    d = json.load(json_data)
    print(d["Records"][0]["s3"]["bucket"]["arn"])
