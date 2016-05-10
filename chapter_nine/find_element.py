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




if __name__ == '__main__':
    array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    find_element = FindElement(array)
    print find_element.array
    # find_element.find()