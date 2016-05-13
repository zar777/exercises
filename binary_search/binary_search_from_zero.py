import random

class BinarySearchFromZero(object):
    """this class is created to represent a sorted array which will be applied binary search algorithm"""

    def __init__(self, sorted_array):
        self.array = sorted_array

    def binary_search_from_zero_algorithm(self, first, last, key):
        """this method is created to search an element in sorted array, given a key"""
        mid = (first + last) / 2
        if (mid == len(self.array)-1 and key != self.array[mid]) or key < self.array[first]:
            return -1
        if key == self.array[mid]:
            return mid
        if key > self.array[mid]:
            new_last = last*2
            if new_last < len(self.array):
                return self.binary_search_from_zero_algorithm(last, new_last, key)
            # elif new_last > len(self.array):
            #     return self.binary_search_from_zero_algorithm(last, len(self.array)-1, key)
            else:
                return self.binary_search_from_zero_algorithm(mid, len(self.array), key)
        else:
            return self.binary_search_from_zero_algorithm(first, mid, key)

if __name__ == '__main__':
    array = [2, 16, 19, 20, 25, 1, 3, 99, 100]
    # array = [1, 2, 3]
    # array = [1, 2, 3, 4, 5, 6, 100, 110, 120, 130, 150]
    # array = [2, 6, 7, 10, 20, 30, 40, 50]
    # array = [1, 2]
    array.sort()
    print array
    binary = BinarySearchFromZero(array)
    print binary.array
    print len(binary.array)
    ciao = binary.binary_search_from_zero_algorithm(0, 1, 4)
    print ciao