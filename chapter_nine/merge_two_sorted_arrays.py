"""You are given two sorted arrays, A and B, and A has a large enough buffer at the end
to hold B. Write a method to merge B into A in sorted order. Exercises 9.1"""

import random

class MergeTwoSortedArrays(object):
    def __init__(self, array_one, array_two):
        self.array_one = array_one
        self.array_two = array_two

    # def merge(self):
    #
    #     buffer_array_one = []
    #     i = 0
    #     while self.array_one[i] is not None:
    #         buffer_array_one.insert(i, self.array_one[i])
    #         i += 1
    #     while len(buffer_array_one) != 0 and len(self.array_two) != 0:
    #         if(buffer_array_one[0] < self.array_two[0]):
    #             self.array_one[i] = buffer_array_one.pop(0)
    #             i += 1
    #         else:
    #             self.array_one[i] = array_two.pop(0)
    #             i += 1
    #     while len(buffer_array_one) != 0:
    #         self.array_one[i] = buffer_array_one.pop(0)
    #     while len(self.array_two) != 0:
    #         self.array_one[i] = self.array_two.pop(0)

    def merge(self):

        i = 0
        j = 0
        k = 0
        count = 0
        var = 0
        while self.array_one[k] is not None:
            k += 1
        while j < len(self.array_two):
            if self.array_one[k] is None:
                if self.array_two[j] < self.array_one[i]:
                    swap = self.array_one[i]
                    self.array_one[i] = self.array_two[j]
                    self.array_one[k] = swap
                    j += 1
                    i += 1
                    count += 1
                else:
                    i += 1
            else:
                if i != k:
                    if self.array_two[j] < self.array_one[k]:
                        swap = self.array_one[i]
                        self.array_one[i] = self.array_two[j]
                        self.array_one[k + 1] = swap
                        count += 1
                        j += 1
                        i += 1
                        var += 1
                    else:
                        swap = self.array_one[i]
                        self.array_one[i] = self.array_one[k]
                        self.array_one[k + var] = swap
                        var += 1
                        i += 1
                        count += 1
                else:
                    self.array_one[i] = self.array_two[j]
                    k += var
                    j += 1
                    i += 1


if __name__ == '__main__':
    # array_one = random.sample(range(1, 100), 4)
    # array_two = random.sample(range(1, 100), 4)
    # print array_one
    # print array_two
    # array_one.sort()
    # array_two.sort()
    array_one = [24, 33, 44, 89, None, None, None, None]
    array_two = [4, 44, 45, 88]
    class_merge = MergeTwoSortedArrays(array_one, array_two)
    print class_merge.array_one
    print class_merge.array_two
    print class_merge.merge()
    print class_merge.array_one