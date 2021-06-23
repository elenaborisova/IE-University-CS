def main():
    n1, n2, n3, n4, n5 = eval(input('Enter 5 numbers separated by comma: '))

    numbers_sum = n1 + n2 + n3 + n4 + n5
    numbers_average = numbers_sum // 5

    print('Sum of numbers:', numbers_sum)
    print('Average of numbers:', numbers_average)


main()
