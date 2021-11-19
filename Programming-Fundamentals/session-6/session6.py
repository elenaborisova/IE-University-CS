# -*- coding: utf-8 -*-

#%%

my_file = open('hello.txt')

for line in my_file:
    print(line)

my_file.close()


#%%

with open('hello.txt') as file:
    for line in file:
        print(line)


#%%

letter = 'Dear Whoever...'

with open('letter.txt', 'w') as file:
    file.write(letter)


#%%

import csv

programs = [
    ['MCSBT', 'Masters in Computer Science and Business Technology'],
    ['MDBI', 'Masters in Digital Business and Innovation'],
]

with open('programs.csv', 'w') as file:
    writer = csv.writer(file)

    for program in programs:
        writer.writerow(program)


#%%

with open('programs.csv') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line[0])


#%%

import json

with open('data/data.json') as file:
    data = json.load(file)
    # print(type(data))  # list

    for element in data:
        print(element['_id'])


#%%

programs = {
    'MDBI': 'Masters in Digital Business and Innovation',
    'MCSBT': 'Masters in Computer Science and Business Technology',
}

with open('programs.json', 'w') as file:
    json.dump(programs, file)
    # data = json.dumps(programs)  # returns a string

