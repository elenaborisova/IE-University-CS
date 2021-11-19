def bubble_sort(lst):
    is_sorted = True

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False
        if is_sorted:
            break

    return lst


print(bubble_sort([1, 2, 3, 8, 6, 4]))

# Time: O(n^2); Space: O(1)


# Using while loop
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort2(lst):
    for el in lst:
        i = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)
            i += 1
