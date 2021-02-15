"""Write a method to return all subsets of a set"""


def subset_of_set(my_set, i, j):
    if i > j:
        pass
    if i == j:
        if len(my_set) == 1:
            pass
        else:
            print str(my_set[i])
            subset_of_set(my_set, i + 1, len(my_set) - 1)
    if i < j:
        if len(my_set) == 2:
            subset_of_set(my_set, i, j - 1)
        else:
            print str(my_set[i]) + "," + str(my_set[j])
            subset_of_set(my_set, i, j - 1)


if __name__ == '__main__':
    array = [2, 4, 55, 1]
    # array = [2, 4, 55]
    # array = [2]
    # array = [2, 4]
    # set_of_array = set(array)
    subset_of_set(array, 0, len(array)-1)
