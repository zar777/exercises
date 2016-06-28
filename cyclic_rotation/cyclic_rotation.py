"""
Rotate an array to the right by a given number of steps.
"""


def solution(A, K):
    array_solution = [None]*len(A)
    count = len(A)
    index = 0
    
    if K % len(A) == 0 or K == 0:
        array_solution = A
    else:
        while count >= 0:
            new_index = index+K
            if new_index < len(A):
                array_solution[new_index] = A[index]
                index = new_index
                count -= 1
            else:
                while new_index >= len(A):
                    new_index -= len(A)
                array_solution[new_index] = A[index]
                index = new_index
                count -= 1
    return array_solution


if __name__ == '__main__':
    array = [3, 8, 9, 7, 6]
    print solution(array, 100)
