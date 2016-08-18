# import sys
#
# first_line = sys.stdin.readline().split(" ")
# len_array = int(first_line[0])
# rotations = int(first_line[1])
# array = sys.stdin.readline().split(" ")
# i = 0
# for index in xrange(len_array):
#     new_index = (i+rotations)-len_array
#     tmp = array[new_index]
#     array[(index+rotations)-len_array] = array[i]
#     i = new_index
# print array


import sys
from collections import deque

# second solution
first_line = sys.stdin.readline().split(" ")
array = deque(sys.stdin.readline().split(" "))
array.rotate(-int(first_line[1]))
print " ".join(array)

