class AlmostFibonacciKnapsack(object):
    def getIndices(self, x):
        array = [1,2,3]
        el = 1
        find = 2
        while find + array[el+1] < x:
            find = array[el] + array[el + 1] - 1
            array.append(find)
            el +=1
        return array

if __name__ == '__main__':
    a = AlmostFibonacciKnapsack()
    print a.getIndices(148)
