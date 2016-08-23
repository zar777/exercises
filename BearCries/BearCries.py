import re

class BearCries(object):

    def count(self, message):
        split = message.split()
        if message.count(";") % 2 == 1 or (split[0] or split[-1]) == '_':
            return 0
        count = len(re.findall(r"\;(.*)(\_+)(.*)\;", message))
        return count

if __name__ == '__main__':
    s = "_;__;"
    a = BearCries()