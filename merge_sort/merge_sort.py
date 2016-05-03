import random

class MergeSort(object):
    """this class is created to represent an unsorted array which will be applied merge sort algorithm"""

    def __init__(self, unsorted_array):
        self.array = unsorted_array

    def merge_sort_algorithm(self, low, high):
        """this method is created to order an unsorted array, through Divide-and-Conquer method"""
        if low < high:
            mid = low + high / 2
            self.merge_sort_algorithm(low, mid)
            self.merge_sort_algorithm(mid+1, high)
            self.merge(low, high, mid)

    def merge(self, low, high, mid):
        array_one = []
        array_two = []

        for element in range(low, mid):
            array_one.append(self.array[element])
        for element in range(mid+1, high):
            array_two.append(self.array[element])
        i = 0
        while array_one != [] and array_two != []:
            if array_one[i] < array_two[i]:
                self.array[i] = array_one.pop(0)
            else:
                self.array[i] = array_two.pop(0)

        while(svuotare array1)

        while(svuotre array2)

        return True
if __name__ == '__main__':
    array = random.sample(range(1, 100), 10)
    print array
    merge = MergeSort(array)
    print merge.array
    print len(merge.array)
    print merge.merge_sort_algorithm(0, len(merge.array))
