class BinarySearch(object):
    """this class is created to represent a sorted array which will be applied binary search algorithm"""

    def __init__(self, sorted_array):
        self.array = sorted_array

    def binary_search_algorithm(self, first, last, key):
        """this method is created to search an element in sorted array, given a key"""
        if first > last:
            return -1
        mid = (first + last) / 2
        if key == self.array[mid]:
            return mid
        if key > self.array[mid]:
            return self.binary_search_algorithm(mid+1, last, key)
        else:
            return self.binary_search_algorithm(first, mid - 1, key)

if __name__ == '__main__':
    array = [20, 30, 40, 50]
    print array
    binary = BinarySearch(array)
    print binary.array
    print len(binary.array)
    ciao = binary.binary_search_algorithm(0, len(binary.array), 30)
    print ciao