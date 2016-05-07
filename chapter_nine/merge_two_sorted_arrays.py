import random

class MergeTwoSortedArrays(object):
    def __init__(self, array_one, array_two):
        self.array_one = array_one
        self.array_two = array_two

    def merge(self):

        buffer_array_one = []
        i = 0
        while self.array_one[i] is not None:
            buffer_array_one.insert(i, self.array_one[i])
            i += 1
        while len(buffer_array_one) != 0 and len(self.array_two) != 0:
            if(buffer_array_one[0] < self.array_two[0]):
                self.array_one[i] = buffer_array_one.pop(0)
                i += 1
            else:
                self.array_one[i] = array_two.pop(0)
                i += 1
        while len(buffer_array_one) != 0:
            self.array_one[i] = buffer_array_one.pop(0)
        while len(self.array_two) != 0:
            self.array_one[i] = self.array_two.pop(0)



if __name__ == '__main__':
    # array_one = random.sample(range(1, 100), 4)
    # array_two = random.sample(range(1, 100), 4)
    # print array_one
    # print array_two
    # array_one.sort()
    # array_two.sort()
    array_one = [36, 63, 67, 89, None, None, None, None]
    array_two = [4, 36, 64, 76]
    class_merge = MergeTwoSortedArrays(array_one, array_two)
    print class_merge.array_one
    print class_merge.array_rwo
