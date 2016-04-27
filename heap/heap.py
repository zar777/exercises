class Heap(object):
    """this class is created to represent a Heap and all useFull methods for clients"""

    def __init__(self, n):

        self.priority_queue = None

        if self.priority_queue is None:

            self.elements = 0
        else:

            self.elements = n

    def make_heap(self, array, n):

        heap = self.priority_queue

        for element in range(1, n):

            self.insert(heap, array[element])

    def insert(self, priority_queue, arrayelement):





    def bubble_up(self):
        pass



    def swap(self):

        pass



    def bubble_down(self):

        pass



    def extract_min(self):

        pass

    def parent(self, element):

        if element == 1:
            return None
        else:
            return element/2



    def young_child(self, parent):

        return 2*parent


    def __str__(self):

        stringheap = str(self.priority_queue)

        return stringheap

    def __len__(self):

        return self.elements



if __name__ == '__main__':
    n = 5
    array = []
    array = array + [1]
    array = array + [77]
    array = array + ["Ciao"]
    array = array + [25]
    array = array + [99]
    array = array + [27]
    print array
    heap = Heap(n)
    print heap
    print heap.__len__()
