import csv
import os
import json


def convert_format():
    with open((os.path.relpath('../data/data.csv'))) as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

        with open('converted.json', 'w') as json_file:
            json.dump(data, json_file)


convert_format()
