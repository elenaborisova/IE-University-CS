def linear_search(value, elements):
    for element in elements:
        if value == element:
            return True

    return False


print(linear_search(5, [1, 2, 3, 5]))

