def main():
    print('Welcome to the Factorial Generator\n')

    n = int(input('Please enter a whole number: '))

    fact = 1

    for i in range(n, 0, -1):
        fact *= i

    print('\nThe factorial of', n, 'is', fact)


main()
