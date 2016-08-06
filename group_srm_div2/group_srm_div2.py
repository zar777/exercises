class GroupSRMDiv2(object):
    def FindGroups(self, t):
        occurrences = {}
        count = 1
        for member in t:
            if member not in occurrences:
                occurrences[member] = count
            else:
                occurrences[member] += 1
        groups = 0
        for el in occurrences:
            if occurrences[el] % el != 0:
                return -1
            else:
                groups += occurrences[el] / el
        return groups


if __name__ == '__main__':
    members = [2,2,3,3,3]
    c = GroupSRMDiv2()
    print c.FindGroups(members)