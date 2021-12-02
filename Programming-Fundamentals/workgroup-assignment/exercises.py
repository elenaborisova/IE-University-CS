# %%
# Exercise 1:
def max_between(lst, i, j):
    # Indices Validation (assuming first index < second index)
    if not 0 <= i < len(lst) or not 0 <= j < len(lst) or j <= i:
        return 'Invalid Index!'

    max_num = lst[i]

    for index in range(i + 1, j + 1):
        if lst[index] > max_num:
            max_num = lst[index]

    return max_num


# Time complexity: O(n), Space complexity: O(1)

# Test Cases:
print(max_between([4, 2, 6, 7, 10, 1], 0, 5))  # 10
print(max_between([4, 2, 6, 7, 10, 1], 0, 6))  # Invalid Index!
print(max_between([4, 2, 6, 7, 10, 1], -1, 5))  # Invalid Index!
print(max_between([4, 2, 6, 7, 10, 1], 5, 0))  # Invalid Index!
print(max_between([4, 2, 6, 7, 10, 1], 0, 0))  # Invalid Index!
print(max_between([], 1, 20))  # Invalid Index!


"""
Can you think of a faster implementation of your algorithm if you're ensured that the list is sorted? 

If the list is sorted, we know that the greatest value is at the end of the list, if the sorting is ascending.
Hence, we want to return the value at index j (or the second index that our function receives as a parameter),
as this will be the maximum value in the specified range.

This would reduce Time complexity to O(1).
"""


# %%
# Exercise 2:
def appears_in_both(nums1, nums2, value):
    # Time complexity: O(n); Space complexity O(1)
    for num in nums1:
        if num == value:
            break
    else:
        return False

    for num in nums2:
        if num == value:
            return True
    return False


def appears_in_both_sorted(nums1, nums2, value):
    # Time complexity: O(log n); Space complexity O(1)

    # Assuming ascending sorting order
    if nums1[0] > value or nums2[0] > value or nums1[-1] < value or nums2[-1] < value:
        return False

    return binary_search(nums1, value) and binary_search(nums2, value)


def binary_search(lst, value):
    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_val = lst[mid_idx]

        if mid_val == value:
            return True
        elif value < mid_val:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1

    return False


# Test Cases:
print(appears_in_both_sorted([1, 2, 3], [4, 5, 6], 7))  # False
print(appears_in_both_sorted([1, 2, 3], [3, 5, 6], 3))  # True
print(appears_in_both([1, 3, 2], [3, 19, 6], 3))  # True
print(appears_in_both([1, 3, 2], [3, 19, 6], 29))  # False

# %%
# Exercise 3:


def lists_intersection_without_duplicates(list1, list2):
    return [el for el in set(list1) if el in list2]


def lists_intersection_with_duplicates(list1, list2):
    return [el for el in list1 if el in list2]


# Time complexity: O(n^2); Space complexity: O(n)

# Test Cases:
print(lists_intersection_without_duplicates([1, 2, 3, 4, 4], [4, 4, 5, 6]))  # [4]
print(lists_intersection_with_duplicates([1, 2, 3, 4, 4], [4, 4, 5, 6]))  # [4, 4]
print(lists_intersection_with_duplicates([1, 2, 3], [4, 5, 6]))  # []
print(lists_intersection_with_duplicates([], []))  # []


"""
Could you find a faster implementation if you're sure that the two lists you receive are sorted?

If the two lists are not sorted, then the time complexity is O(N x M) or O(N^2) if the lists are of equal length.
This is because we iterate through the first list, and then check with linear search whether the element is in the second list.
If we know that the two lists are sorted, instead of doing linear search, we can implement binary search,
which would reduce the time complexity to O(M x log N) or O(N x log N) if the are of equal length.

Also, we can further optimize the algorithm if we add an additional if-statement in the beginning of the function.
We can check which list is the smaller and iterate through it first, and implement the binary search on the larger one.
"""


# %%
# Exercise 4:
def difference_with_duplicates(list1, list2):
    different_elements1 = [el for el in list1 if el not in list2]
    different_elements2 = [el for el in list2 if el not in list1]

    return different_elements1 + different_elements2


def difference_without_duplicates(list1, list2):
    return set(difference_with_duplicates(list1, list2))


# Time complexity: O(n^2); Space complexity: O(n)


# Test Cases:
print(difference_with_duplicates([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(difference_with_duplicates([1, 2, 3, 4, 4], [4, 4, 5, 6]))  # [1, 2, 3, 5, 6]
print(difference_without_duplicates([1, 2, 3, 4, 4], [5, 6]))  # {1, 2, 3, 4, 5, 6}
print(difference_with_duplicates([1, 2, 3, 4, 4], [5, 6]))  # [1, 2, 3, 4, 4, 5, 6]


"""
Could you find a faster implementation if you're sure that the two lists you receive are sorted?

Same as in the previous problem, if the lists are sorted, we can implement a binary search when looking 
if an element from the first list is not present in the second one and vise versa, 
in order to decrease the time complexity to O(n log n).
"""


# %%
# Exercise 5:
def dictionary_lookup(dictionaries, word):
    for dictionary in dictionaries:
        if dictionary['word'] == word:
            return dictionary['definition']
    return None


# Time complexity: O(n); Space complexity: O(1)


"""
What's the worst case runtime for your algorithm? Why so?

The worst case runtime is linear O(n), when the word we are looking for is either in the very last position 
of the dictionary or it does not exist at all. 
Looking up a key in the dictionary takes O(1) constant time, so this does not add to the complexity.
"""
