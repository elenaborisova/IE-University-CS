import math


def main():
    diameter = float(input('Enter the diameter: '))
    price = float(input('Enter the price: '))
    radius = diameter / 2

    area = math.pi * radius ** 2
    cost_per_inch = price / area

    print('The cost per square inch of a circular pizza is:', cost_per_inch)


main()
