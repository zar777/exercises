# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(A):
    peak = []
    blocks = 0
    for i in xrange(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peak.append(i)
    divisors = int(math.sqrt(len(A)))
    while divisors > 0:
        if len(A) % divisors == 0:
            multi = len(A) / divisors
            first = 0
            count = 0
            while multi <= len(A):
                any_in = 0
                if lambda a, b: any(i in xrange(first, multi) for i in peak):
                    first = multi
                    multi += len(A) / divisors
                    count += 1
                else:
                    multi == len(A)
            if count == divisors:
                blocks += 1
            divisors -= 1
    return blocks


    return peak

if __name__ == '__main__':
    A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    print solution(A)