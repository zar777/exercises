"""Given an array of ages (integers) sorted lowest to highest, output the number of occurrences for each age.
The algorithm should take less than O(n) in time, where n is the length of the array.
Input: [8,8,8,9,9,11,15,16,16,16]
Output: {8: 3, 9: 2, 11: 1, 15: 1, 16:3}
"""


def binary_search_algorithm_left(array, first, last, key):
    if first > last:
        return last
    mid = (first + last) / 2

    if key > array[mid]:
        return binary_search_algorithm_left(array, mid + 1, last, key)
    else:
        return binary_search_algorithm_left(array, first, mid - 1, key)


def binary_search_algorithm_right(array, first, last, key):
    if first > last:
        return last
    mid = (first + last) / 2

    if key >= array[mid]:
        return binary_search_algorithm_right(array, mid + 1, last, key)
    else:
        return binary_search_algorithm_right(array, first, mid - 1, key)


def occurrence_ages_n_complexity(array):
    dict = {}
    for age in array:
        if age in dict:
            dict[age] += 1
        else:
            dict[age] = 1

    return dict

def occurrence_ages(array):
    dict = {}
    for age in array:
        left = binary_search_algorithm_left(array, 0, len(array) - 1, age)
        right = binary_search_algorithm_right(array, 0, len(array) - 1, age)
        dict[age] = right - left
        del array[left:right-1]
    return dict

if __name__ == '__main__':
    array = [8, 8, 8, 9, 9, 11, 15, 16, 16, 16]
    print occurrence_ages_n_complexity(array)
    print occurrence_ages(array)