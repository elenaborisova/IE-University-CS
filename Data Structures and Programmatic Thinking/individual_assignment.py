def calculate_cylinder_volume(radius, height, pi):
    return pi * radius ** 2 * height


def calculate_sphere_volume(radius, pi):
    return 4/3 * pi * radius ** 3


def print_cylinder_volume(pi):
    radius = float(input('What is the cylinder radius? '))
    height = float(input('What is the cylinder height? '))
    print(calculate_cylinder_volume(radius, height, pi))


def print_sphere_volume(pi):
    radius = float(input('What is the sphere radius? '))
    print(calculate_sphere_volume(radius, pi))


def get_multiples():
    return [n for n in range(1001) if n % 5 == 0 and n % 3 == 0]


pi = 3.14
