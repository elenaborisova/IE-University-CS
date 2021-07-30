def get_min_value(values):
    return min(values)


def get_max_value(values):
    return max(values)


def get_values():
    values = []
    while len(values) < 5:
        try:
            val = float(input('Please enter a number: '))
            values.append(val)
        except ValueError:
            print('Please enter only numerical values!')

    return values


def main():
    values = get_values()
    min_value = get_min_value(values)
    max_value = get_max_value(values)

    print('Min value is:', min_value)
    print('Max value is:', max_value)


main()
