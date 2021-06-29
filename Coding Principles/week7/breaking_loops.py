def main():
    while True:
        num = float(input('Enter a positive number: '))
        if num >= 0:
            break
        else:
            print('The number you entered was not positive')

    print('The number you entered was ', num)


main()
