import timeit


def find_max_element(nums):
    max_num = None

    for num in nums:
        if max_num is None or num > max_num:
            max_num = num

    return max_num


def timer():
    find_max_element([1, 2, 3, 4, 2, 4, 1])


print(timeit.timeit(timer))
