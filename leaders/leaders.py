# 
# Task description
# A non-empty zero-indexed array A consisting of N integers is given.
# 
# The leader of this array is the value that occurs in more than half of the elements of A.
# 
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
# 
# For example, given array A such that:
# 
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
# 
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count_max_occ the number of equi leaders.
# 
# Write a function:
# 
# def solution(A)
# that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.
# 
# For example, given:
# 
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.
# 
# Assume that:
# 
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Complexity:
# 
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

# Exercises DONE : time : 60 minutes / result 100 %

# count_max_occ all the occurrences in a list with dictionary, find if exist 1 leader into a dict and if exist,
# I search in the list whenever if the LEADER maintains its leadership into the two subdivision of the list.
import operator


def solution(A):
    counter = {}
    equi_leaders = 0
    for e in A:
        if e in counter:
            counter[e] += 1
        else:
            counter[e] = 1
    maxval = max(counter.iteritems(), key=operator.itemgetter(1))[1]
    keys = [k for k, v in counter.items() if v == maxval]
    if len(keys) == 1:
        count_max_occ = 0
        for i, e in enumerate(A, 1):
            if e == keys[0]:
                count_max_occ += 1
            if count_max_occ > i/2 and maxval - count_max_occ > (len(A)-i)/2:
                equi_leaders += 1
    else:
        return equi_leaders
    return equi_leaders

if __name__ == '__main__':
    A = [4, 3, 4, 4, 4, 2]
    print solution(A)

