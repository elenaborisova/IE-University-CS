def end_of_file():
    file_name = input('What file are the numbers in? ')
    in_file = open(file_name, 'r')

    total = 0.0
    count = 0

    line = in_file.readline()
    while line:
        total += float(line)
        count += 1

        line = in_file.readline()

    print(total / count)


def loaded_file():
    file_name = input('What file are the numbers in? ')
    in_file = open(file_name, 'r')

    total = 0.0
    count = 0

    for line in in_file:
        total += float(line)
        count += 1

    average = total / count
    print(average)


def nested_loops_with_split():
    file_name = input('What file are the numbers in? ')
    in_file = open(file_name, 'r')

    total = 0.0
    count = 0

    line = in_file.readline()
    while line:
        for x_str in line.split(', '):
            x = float(x_str)
            total += x
            count += 1

        line = in_file.readline()

    print(total/count)


nested_loops_with_split()
