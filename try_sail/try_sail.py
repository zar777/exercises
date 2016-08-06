import operator


class TrySail(object):

    def get(self, strength):
        sum_st = 0
        for index, el in enumerate(strength, 0):

            operator.xor(el, strength[index+1])
        return sum_st

if __name__ == '__main__':
    strength = [7,3,5,2]
    trysail = TrySail()
    print trysail.get(strength)