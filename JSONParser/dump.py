obj = [{'name': 'ABC', 'Age': '21', 'Address': {'Street': '1', 'More details': {'City': 'Hyd', 'State': 'Telangana'}}}]
with open("dump.json", "w") as file:
    data = str(obj)
    data = data.replace("'", "\"")
    print(data)
    file.write(data)