import math


def calculate_circle_volume(r):
    return math.pi * (r ** 2)


def calculate_triangle_volume(b, h):
    return 1/2 * b * h


def calculate_cube_volume(s):
    return s ** 3


def main():
    while True:
        try:
            shape = int(input('Please enter a number corresponding to a shape:\n'
                              '(1) Circle\n(2) Triangle\n(3) Cube:\n'))

            if shape == 1:
                print('You chose (1) Circle')

                radius = input('Please enter the radius of the circle: ')
                while radius.isalpha() or not radius or float(radius) <= 0:
                    print('Your input should be a positive numerical value!')
                    radius = input('Please enter the radius of the circle: ')

                radius = float(radius)
                circle_volume = calculate_circle_volume(radius)
                print('The circle volume is:', circle_volume)
                break
            elif shape == 2:
                print('You chose (2) Triangle')

                base = input('Please enter the base of the triangle: ')
                height = input('Please enter the height of the triangle: ')
                while base.isalpha() or height.isalpha() \
                        or not base or not height \
                        or float(base) <= 0 or float(height) <= 0:
                    print('Both of your inputs should contain positive numerical values!')
                    base = input('Please enter the base of the triangle: ')
                    height = input('Please enter the height of the triangle: ')

                base = float(base)
                height = float(height)
                triangle_volume = calculate_triangle_volume(base, height)
                print('The volume of the triangle is:', triangle_volume)
                break
            elif shape == 3:
                print('You chose (3) Cube')

                length = input('Please enter the length of the cube side: ')
                while length.isalpha() or not length or float(length) <= 0:
                    print('Your input should be a positive numerical value!')
                    length = input('Please enter the length of the cube side: ')

                length = float(length)
                cube_volume = calculate_cube_volume(length)
                print('The volume of the cube is:', cube_volume)
                break

            else:
                print('Only the numbers 1, 2, and 3 are accepted!')

        except ValueError:
            print('Your input should be a numerical value 1, 2, or 3!\n')


main()
