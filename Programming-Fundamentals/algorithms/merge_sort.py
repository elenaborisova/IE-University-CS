def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid_idx = len(lst) // 2
    left = merge_sort(lst[:mid_idx])
    right = merge_sort(lst[mid_idx:])

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result


print(merge_sort([]))
