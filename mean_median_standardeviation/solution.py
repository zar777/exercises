import math


def mean(a):
    return int(round(float(sum(a)) / float(len(a))))


def median(a):
    a.sort()
    return a[len(a)/2] if len(a) % 2 != 0 else (a[len(a)/2] + a[(len(a)/2)-1]) / 2


def standard_deviation(a):
    var = variance(a)
    return math.sqrt(var)


def variance(a):
    m = mean(a)
    tmp = 0
    for el, i in enumerate(a, 0):
        tmp += math.sqrt(abs(el - m))
    tmp /= len(a)
    return tmp

if __name__ == '__main__':
    a = [20, 55, 2, 1, 11, 47]
    print standard_deviation(a)