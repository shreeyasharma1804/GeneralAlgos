# JSON Loader for Python
# Support for arrays and nested objects 
# Uses recursion

class JSON_Parser:

    def __init__(self):
        self.lines = []
        self.index = 0
        self.all_documents = []
        self._load_data()

    def _remove_comma(self, value):
        if(isinstance(value, str)):
            value = value.strip(",")
        return value

    def _remove_quotes(self, value):
        if(isinstance(value, str)):
            value = value.strip("\"")
        return value

    def _string_cleanup(self, value):
        value = self._remove_comma(value)
        value = self._remove_quotes(value)
        return value

    def _load_data(self):
        with open('load.json', 'r') as json_file:
            for line in json_file:
                self.lines.append(line.strip())

    def _load(self, entry):
        if(self.lines[self.index][0] == "{"):
            self.index += 1
            return self._load(entry)
        elif(self.lines[self.index][0] == "}"):
            return entry
        else:
            key_and_value = self.lines[self.index].split(":")
            key = key_and_value[0].strip()
            value = key_and_value[1].strip()
            if(value.startswith("{")):
                self.index += 1
                value = self._load({})
            key = self._string_cleanup(key)
            value = self._string_cleanup(value)
            entry[key] = value
            self.index += 1
            return self._load(entry)

    def load(self):

        while self.index < len(self.lines):
            if(self.lines[self.index][0] != "[" and self.lines[self.index][0] != "]"):
                self.all_documents.append(self._load({}))
            self.index += 1

        return self.all_documents

    def stringify(self, obj):
        data = str(obj)
        data = data.replace("'", "\"")
        return data
    
    def dump(self, obj):
        data = self.stringify(obj)
        with open("dump.json", "w") as file:
            file.write(data)

json_parser = JSON_Parser()
json_obj = json_parser.load()

print(json_obj)

json_parser.dump(json_obj)