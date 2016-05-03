class BinarySearch(object):
    """this class is created to represent a sorted array which will be applied binary search algorithm"""

    def __init__(self, sorted_array):
        self.array = sorted_array

    def binary_search_algorithm(self, first, last, key):
        """this method is created to search an element in sorted array, given a key"""
        if first > last:
            return -1
        mid = (first + last) / 2
        if key == mid:
            return self.array[key]
        if key > mid:
            self.binary_search_algorithm(mid+1, last, key)
        else:
            self.binary_search_algorithm(first, mid - 1, key)

if __name__ == '__main__':
    array = range(0, 20)
    print array
    binary = BinarySearch(array)
    print binary.array
    print len(binary.array)
    print binary.binary_search_algorithm(0, len(binary.array), 8)