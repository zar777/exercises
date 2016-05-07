import random

class MergeSort(object):
    """this class is created to represent an unsorted array which will be applied merge sort algorithm"""

    def __init__(self, unsorted_array):
        self.array = unsorted_array

    def merge_sort_algorithm(self, low, high):
        """this method is created to order an unsorted array, through Divide-and-Conquer method"""
        if low < high:
            mid = (low + high) / 2
            self.merge_sort_algorithm(low, mid)
            self.merge_sort_algorithm(mid+1, high)
            self.merge(low, high, mid)

    def merge(self, low, high, mid):
        """this method is created to order and merge an unsorted array, through two buffers"""
        array_one = []
        array_two = []

        for element in range(low, mid+1):
            array_one.append(self.array[element])
        for element in range(mid+1, high+1):
            array_two.append(self.array[element])

        i = low

        while len(array_one) != 0 and len(array_two) != 0:
            if array_one[0] <= array_two[0]:
                self.array[i] = array_one.pop(0)
                i += 1
            else:
                self.array[i] = array_two.pop(0)
                i += 1

        while len(array_one) != 0:
            self.array[i] = array_one.pop(0)
            i += 1

        while len(array_two) != 0:
            self.array[i] = array_two.pop(0)
            i += 1

if __name__ == '__main__':
    array = random.sample(range(1, 100), 10)
    print array
    merge = MergeSort(array)
    print merge.array
    array.sort()
    print array
    print merge.array
    print len(merge.array)
    print merge.merge_sort_algorithm(0, len(merge.array)-1)
    print merge.array
