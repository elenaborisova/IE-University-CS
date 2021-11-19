import json
import os.path


with open((os.path.relpath('../data/luke.json'))) as file:
    data = json.load(file)
    print(data)

    print('Name: ' + data['name'])
    print('Height: ' + data['height'])
    print('Eye color: ' + data['eye_color'])
    print('Mass: ' + data['mass'])
