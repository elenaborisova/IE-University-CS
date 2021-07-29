from math import sqrt


def get_numbers():
    nums = []

    num_str = input()
    while num_str:
        num = float(num_str)
        nums.append(num)

        num_str = input()

    return nums


def find_mean(nums):
    total = 0

    for num in nums:
        total += num

    return total / len(nums)


def find_std_dev(nums, xbar):
    sum_dev_sq = 0

    for num in nums:
        dev = num - xbar
        sum_dev_sq += dev * dev

    return sqrt(sum_dev_sq / len(nums) - 1)


def find_median(nums):
    nums.sort()
    size = len(nums)
    mid_pos = size // 2

    if size % 2 == 0:
        med = (nums[mid_pos] - nums[mid_pos - 1]) / 2
    else:
        med = nums[mid_pos]

    return med


def find_min_num(nums):
    return min(nums)


def find_max_num(nums):
    return max(nums)


def find_average(nums):
    return sum(nums) / len(nums)


def find_variance(nums, xbar):
    return find_std_dev(nums, xbar) ** 2


def main():
    print('This program computes mean, median and standard deviation.')

    data = get_numbers()
    xbar = find_mean(data)
    std = find_std_dev(data, xbar)
    med = find_median(data)
    min_num = find_min_num(data)
    max_num = find_max_num(data)
    average = find_average(data)
    variance = find_variance(data, xbar)

    print(f'\nThe mean is: {xbar}')
    print(f'The standard deviation is: {std}')
    print(f'The median is: {med}')
    print(f'The smallest number is: {min_num}')
    print(f'The biggest number is: {max_num}')
    print(f'The average is: {average}')
    print(f'The variance is: {variance}')


if __name__ == '__main__':
    main()
