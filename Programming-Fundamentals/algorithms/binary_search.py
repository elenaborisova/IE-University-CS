# Iterative approach - Time: O(log N); Space: O(n)
def binary_search(lst, value):
    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_val = lst[mid_idx]

        if mid_val == value:
            return mid_idx
        elif value < mid_val:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1

    return -1


# Recursive approach - Time: O(log N); Space: O(log N)
def binary_search_recursive(lst, left, right, value):
    if right < left:
        return -1

    mid_idx = (right + left) // 2
    mid_val = lst[mid_idx]

    if mid_val == value:
        return mid_idx
    elif value < mid_val:
        return binary_search_recursive(lst, left, mid_idx - 1, value)
    else:
        return binary_search_recursive(lst, mid_idx + 1, right, value)


nums = [1, 2, 3, 4, 5, 6, 7]
print(binary_search_recursive(nums, 0, len(nums) - 1, 6))
