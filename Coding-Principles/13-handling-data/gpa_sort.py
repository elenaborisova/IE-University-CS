from gpa import Student, makeStudent


def read_students(file_name):
    in_file = open(file_name, ' r')
    students = []

    for line in in_file:
        students.append(makeStudent(line))
        in_file.close()
        return students


def write_students(students, file_name):
    out_file = open(file_name, 'w')

    for s in students:
        print(f'{s.getName()}\t{s.getHours()}\t{s.getPoints()}', file=out_file)

    out_file.close()


def main():
    print('This program sorts student grade information by GPA')
    file_name = input()
    data = read_students(file_name)
    data.sort(key=Student.gpa)
    file_name = input('Enter a name for the output file: ')
    write_students(data, file_name)
    print('The data has been written to:', file_name)


if __name__ == '__main__':
    main()
