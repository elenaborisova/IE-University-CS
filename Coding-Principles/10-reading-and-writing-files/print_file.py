def main():
    file_name = input('Enter file name: ')
    in_file = open(file_name, 'r')
    data = in_file.read()
    print(data)

    in_file.close()


main()
