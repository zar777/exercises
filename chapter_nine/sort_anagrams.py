class SortAnagrams(object):
    def __init__(self, unsorted_array):
        self.array = unsorted_array

    def order_anagrams(self, string):

        return ''.join(sorted(string))


if __name__ == '__main__':
    array = ["rito", "tori", "zxy", "trio", "irto", "orti", "xab",  "xyz", "abx", "xba", "yzx"]
    sort_anagrams = SortAnagrams(array)
    print array
    sort_anagrams.array.sort(key=sort_anagrams.order_anagrams)
    print array
