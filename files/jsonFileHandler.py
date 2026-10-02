import json

def readJsonFile(filePath):
    data = ""
    try:
        with open(filePath, 'r') as file:
            jsonData = json.load(file)
            data = jsonData
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error reading file")
    return data