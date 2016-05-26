"""Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. You can exclude the inclusion of 0 in the subsets.
If N=4, output will be {{1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}}
FAILED"""

def combinations_of_numbers(n, array):
    if len(array) == 1:
        pass
    if len(array) == 2:
        print array
    if len(array) > 2:
        a = array[0]
        array[1] += a
        print combinations_of_numbers(n, array[1:len(array)])
        b = array[len(array)-1]
        array[len(array)-2] += b
        print combinations_of_numbers(n, array[0:len(array)-1])

if __name__ == '__main__':
    n = 4
    array = [1, 1, 1, 1]
    print combinations_of_numbers(n, array)
