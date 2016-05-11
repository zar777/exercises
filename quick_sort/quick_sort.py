import random

class QuickSort(object):
    """this class is created to represent an unsorted array which will be applied quick sort algorithm"""

    def __init__(self, unsorted_array):
        self.array = unsorted_array

    def quick_sort_algorithm(self, left, right):
        """this method is created to order an unsorted array, through Divide-and-Conquer method"""
        if left < right:
            pivot_index = self.partition(left, right)
            self.quick_sort_algorithm(left, pivot_index-1)
            self.quick_sort_algorithm(pivot_index+1, right)

    def partition(self, left, right):
        """this method is created to order an unsorted array, through two buffers"""
        pivot_index = left
        left += 1
        if left is not None and right is not None:
            while left <= right:
                if self.array[left] > self.array[pivot_index] > self.array[right]:
                    self.swap(self.array, left, right)
                if self.array[left] <= self.array[pivot_index]:
                    left += 1
                if self.array[right] >= self.array[pivot_index]:
                    right -= 1
            self.swap(self.array, pivot_index, left-1)

        return left-1

    def swap(self, priority_queue, child, parent):
        """this method is created to swap a parent with his child"""
        tmp = priority_queue[parent]
        priority_queue[parent] = priority_queue[child]
        priority_queue[child] = tmp

if __name__ == '__main__':
    array = random.sample(range(1, 100), 10)
    # array = [95, 63, 31, 13, 60]
    print array
    quick = QuickSort(array)
    print quick.array
    # array.sort()
    # print array
    # print quick.array
    # print len(quick.array)
    print quick.quick_sort_algorithm(0, len(quick.array) - 1)
    print quick.array
