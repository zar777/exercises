# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
    if len(A) == 0:
        return 0
    sort_list = A
    sort_list.sort()
    A = sorted(range(len(A)), key=lambda k: A[k])
    for i, el in enumerate(sort_list, 0):
        if i+2 < len(sort_list):
            if (A[i] < A[i+1] < A[i+2]) and el+sort_list[i+1] > sort_list[i+2]:
                return 1
        else:
            return 0
    else:
        return 0

if __name__ == '__main__':
    A = [5, 3, 3]
    print solution(A)
