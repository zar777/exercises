"""Given a sorted array of n integers that has been rotated an unknown number of
times, give an O(log n) algorithm that finds an element in the array. You may assume
that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array) Exercises 9.3"""


from binary_search.binary_search import BinarySearch

class FindElement(BinarySearch):
    def __init__(self, array):
        super(FindElement, self).__init__()
        self.array = array


    def find_first(self, k):
        pass


    def one_sides_binary_search(self, first, last, lenght_array):
        """this method is created to search an element in sorted array, given a key"""
        if first > last:
            return -1
        mid = (first + last) / 2
        if key == self.array[mid]:
            return mid
        if key > self.array[mid]:
            return self.one_sides_binary_search(f, last, key)
        else:
            return self.binary_search_algorithm(first, mid - 1, key)


"""Failed"""

if __name__ == '__main__':
    array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    find_element = FindElement(array)
    print find_element.array
    # find_element.find()