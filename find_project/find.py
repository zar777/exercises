import sys

class Find(object):
    def __init__(self, path):
        self.path = path

    def find(self):
        lista = range(10)
        for e in lista:
            lista[e] = self.path
        return lista


if __name__ == '__main__':
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv[1])
    class_finder = Find(str(sys.argv[1]))
    print class_finder.find()

