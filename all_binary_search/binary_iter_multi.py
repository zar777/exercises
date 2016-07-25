def binary_iter_multi(element, position, offset, array):
    if len(array) == 0:
        return -1
    while offset <= len(array):
        if array[position] == element:
            return position
        if array[position-1] != element and offset / 2 == 0 and position != 0:
            return -1
        if element > array[position]:
            offset *= 2
            position = offset-1
            if offset > len(array):
                position = (offset / 2)+1
                offset = 1
        else:
            position = offset/2
            offset = 1
