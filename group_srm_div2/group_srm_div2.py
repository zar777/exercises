from collections import Counter


class GroupSRMDiv2(object):
    def FindGroups(self, t):
        occurrences = Counter(t)
        groups = 0
        for size, n in occurrences.iteritems():
            if n % size != 0:
                return -1
            groups += n / size
        return groups


if __name__ == '__main__':
    members = [2,2,3,3,3]
    c = GroupSRMDiv2()
    print c.FindGroups(members)