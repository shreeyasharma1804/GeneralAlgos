# JSON is a human readable encoding format (utf-8 encoding)
# load function is used to cread a json file and convert it to a python dictionary
# dump method is used to write to a json file. Entire file is rewritten as appending is npot supported

import json

with open('example.json', 'r') as file:
    data = json.load(file)

print(type(data))