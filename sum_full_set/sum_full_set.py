def binary_search(start, stop, array, el):
    if len(array) == 1:
        if array[0] == el:
            return 0
        else:
            return -1
    if start > stop:
        return -1
    middle = (start+stop)/2
    if array[middle] == el:
        return middle
    if array[middle] < el:
        return binary_search(middle, len(array), array, el)
    else:
        return binary_search(0, middle, array, el)


class SumFullSet(object):
    def isSumFullSet(self, elements):
        sorted(elements)
        for i in xrange(0, len(elements)):
            for j in xrange(i+1, len(elements)):
                el = elements[i] + elements[j]
                if el < elements[0] or el > elements[len(elements)-1]:
                    return "not closed"
                elif el != elements[i] and el != elements[j]:
                    index = None
                    if elements[i] < el < elements[j]:
                        index = binary_search(i+1, j-1, elements[i+1: j], el)
                    elif el > elements[j]:
                        index = binary_search(j+1, len(elements)-1, elements[j: len(elements)], el)
                    else:
                        index = binary_search(0, i-1, elements[0: i], el)

                    if index == -1:
                        return "not closed"
        return "closed"

if __name__ == '__main__':
    elements = [16,0,43,43,-36,-49,-46,-16,40,34,-43,-24,13,-48,45,19,12,0,43,6,26,-23,50,28,-3,21,46,45,-32,-41,0,-27,42,19,47,-36,-21,-1,5,-21,-28,-43,23,-26,-5,21,-41,16,-37,38]
    sum_class = SumFullSet()
    print sum_class.isSumFullSet(elements)