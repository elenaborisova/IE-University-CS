import math


def main():
    print('This is a program that calculate the volume '
          'and surface area of a sphere from its radius.')

    radius = float(input('Enter the radius: '))

    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print('The volume is:', volume, 'and the area is:', area)


main()
