def binary_search_re(element, first, last, array):
    if first > last:
        return -1
    mid = (first + last) / 2
    if array[mid] == element:
        return mid
    if element > array[mid]:
        return binary_search_re(element, mid+1, last, array)
    else:
        return binary_search_re(element, 0, mid-1, array)

