class EllysCandyBags(object):

    def getSize(self, packets):
        occurrences = {}
        count = 1
        list_char = list("".join(packets))
        for char in list_char:
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = count
        total = 0
        for element in occurrences:
            total += occurrences[element] / 2
        return total




if __name__ == '__main__':
    packets = ["FOO", "BAR", "BAZ", "TOPCODER"]
    el = EllysCandyBags()
    print el.getSize(packets)