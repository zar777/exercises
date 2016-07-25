def binary_search_it(element, first, last, array):
    if len(array) == 0:
        return -1
    for e in xrange(first, last):
        if first > last:
            return -1
        mid = (first + last) / 2
        if array[mid] == element:
            return mid
        if element > array[mid]:
            first = mid+1
        else:
            last = mid -1