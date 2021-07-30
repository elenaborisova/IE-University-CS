def get_input_file():
    while True:
        input_file_name = input('Enter input file name: ')
        if '.txt' not in input_file_name:
            print('Invalid name!')
            continue
        else:
            try:
                input_file = open(input_file_name, 'r')
                return input_file
            except FileNotFoundError:
                print('No such file exists in this directory!')
                continue


def get_option():
    while True:
        output_option = input('How do you want to receive the result? [PRINT] or [SAVE] >> ')
        if not output_option == 'PRINT' and not output_option == 'SAVE':
            print('Invalid option!')
            continue
        else:
            return output_option


def get_output_file(output_option):
    if output_option == 'SAVE':
        while True:
            output_file_name = input('Enter output file name: ')
            if '.txt' not in output_file_name:
                print('Invalid name!')
                continue
            else:
                output_file = open(output_file_name, 'w')
                return output_file
    return ''


def convert_gallons_to_liters(gallons):
    return gallons * 3.78541


def main():
    input_file = get_input_file()
    output_option = get_option()
    output_file = get_output_file(output_option)

    for line in input_file:
        gallons = float(line)
        liters = convert_gallons_to_liters(gallons)
        if output_file:
            print(liters, file=output_file)
        else:
            print(liters)


main()
