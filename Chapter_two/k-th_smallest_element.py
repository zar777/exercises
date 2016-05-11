from quick_sort.quick_sort import QuickSort


class KthSmallestElement(QuickSort):
    def __init__(self, array):
        super(KthSmallestElement, self).__init__(array)

    def find(self, left, right,  k):

        pivot_index = self.partition(left, right)

        if pivot_index == k:
            return self.array[pivot_index]
        elif pivot_index > k:
            return self.find(left, pivot_index - 1, k)
        else:
            return self.find(pivot_index + 1, right, k)



if __name__ == '__main__':
    array = [15, 53, 51, 10, 51, 33, 60, 22]
    k = 4
    new_try = KthSmallestElement(array)
    print new_try.find(0, len(new_try.array) - 1, 4)
    print new_try.array
