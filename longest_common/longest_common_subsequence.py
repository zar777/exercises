def longest_common_subsequence(a, b):
    array2D = [[0 for x in xrange(len(a)+1)] for y in xrange(len(b)+1)]
    for i in xrange(1, len(b)+1):
        for j in xrange(1, len(a)+1):
            if a[j-1] == b[i-1]:
                array2D[i][j] = array2D[i-1][j-1]+1
            else:
                array2D[i][j] = max(array2D[i][j-1],  array2D[i-1][j])
    print array2D
    subsequence = ""
    counter = -1
    for i in xrange(1, len(b) + 1):
        for j in xrange(1, len(a) + 1):
            if counter < array2D[i][j]:
                counter = array2D[i][j]
                subsequence += a[j-1]
    return subsequence

if __name__ == '__main__':
    a = "ACBDEA"
    b = "ABCDA"
    print longest_common_subsequence(a, b)