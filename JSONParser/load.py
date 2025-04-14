# JSON Loader for Python
# Support for arrays and nested objects 
# Uses recursion

def remove_comma(value):
    if(isinstance(value, str)):
        value = value.strip(",")
    return value

def remove_quotes(value):
    if(isinstance(value, str)):
        value = value.strip("\"")
    return value

def string_cleanup(value):
    value = remove_comma(value)
    value = remove_quotes(value)
    return value

def parse(entry):
    global index
    if(lines[index][0] == "{"):
        index += 1
        return parse(entry)
    elif(lines[index][0] == "}"):
        return entry
    else:
        key_and_value = lines[index].split(":")
        key = key_and_value[0].strip()
        value = key_and_value[1].strip()
        if(value.startswith("{")):
            index += 1
            value = parse({})
        key = string_cleanup(key)
        value = string_cleanup(value)
        entry[key] = value
        index += 1
        return parse(entry)


json_file = open('example.json', 'r')
lines = []

for line in json_file:
    lines.append(line.strip())

index = 0
all_documents = []

while index < len(lines):
    if(lines[index][0] != "[" and lines[index][0] != "]"):
        all_documents.append(parse({}))
    index += 1