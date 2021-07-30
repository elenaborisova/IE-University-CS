import random


def get_nums_sum(num1, num2, num3):
    return sum([num1, num2, num3])


def get_nums_average(num1, num2, num3):
    return get_nums_sum(num1, num2, num3) / 3


def main():
    num1 = random.randrange(0, 51)
    num2 = random.randrange(0, 51)
    num3 = random.randrange(0, 51)

    nums_sum = get_nums_sum(num1, num2, num3)
    nums_average = get_nums_average(num1, num2, num3)

    print('Numbers sum is:', nums_sum)
    print('Numbers average is:', nums_average)


main()
