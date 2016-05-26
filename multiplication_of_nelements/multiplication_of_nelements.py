"""Write a method that, given an array of integers, will produce another array of same dimensionality whose elements are calculated as the multiplication of all elements except the one at same index in the original array:
Input: [2, 3, 1, 4]
Output: [12, 8, 24, 6]
12 = 3 * 1 * 4
8 = 2 * 1 * 4
24 = 2 * 3 * 4
6 = 2 * 3 * 1
FAILED"""
def multiplication_of_n_elements(array):
    final_array = []
    for x in array:
        array2 = array
        del array2[0]
        recursion(x, array2, final_array)

def recursion(element, array2, final_Array):

    recursion()
