"""Write a function

def solution(A)
that, given a zero-indexed array A consisting of N integers, returns the number of distinct values in array A."""


def solution(A):
    int_dict = {}
    for el in A:
        int_dict[el] = 0
        
    return len(int_dict)
