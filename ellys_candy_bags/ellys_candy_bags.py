from collections import Counter


class EllysCandyBags(object):

    def getSize(self, packets):
        occurrences = Counter("".join(packets))
        total = 0
        for element in occurrences:
            total += occurrences[element] / 2
        return total


if __name__ == '__main__':
    packets = ["FOO", "BAR", "BAZ", "TOPCODER"]
    el = EllysCandyBags()
    print el.getSize(packets)