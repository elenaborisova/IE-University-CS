def main():
    def convert_c_to_f(c_degrees):
        return (c_degrees * 9 / 5) + 32

    print('This program converts Celsius to Fahrenheit.')

    c_degrees = float(input("Enter degrees in Celsius: "))
    f_degrees = convert_c_to_f(c_degrees)

    print("Degrees in Fahrenheit:", f_degrees)


main()
