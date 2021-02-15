"""
Find longest sequence of zeros in binary representation of an integer
"""


def solution(N):
    count = 0
    previous = 0
    one = 0
    while N != 0:

        if one >= 1 and N % 2 == 0:
            count += 1
        elif one >= 1 and N % 2 == 1 and count > 0:
            one = 1
            if previous == 0 or (previous != 0 and previous < count):
                previous = count
            count = 0
        if N % 2 == 1:
            one += 1
        N /= 2
    return previous

if __name__ == '__main__':
    print solution(99)
