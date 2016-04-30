class Heap(object):
    """this class is created to represent a Heap and all useFull methods for clients"""

    def __init__(self, n):
        self.priority_queue = None
        self.elements = n

    def make_heap(self, array, n):
        """this method is to create and populate a Min-Heap"""
        heap_elements = n+1
        self.priority_queue = [0]*heap_elements

        if len(array) == 0:
            raise ValueError("Empty Array ")

        for pointer in xrange(0, n):
            self.insert(self.priority_queue, array[pointer], pointer)

    def insert(self, priority_queue, arrayelement, pointer):
        """this method is created to insert an element in tail on a priority queue(Heap)"""
        queue_pointer = pointer+1
        priority_queue[queue_pointer] = arrayelement
        self.bubble_up(priority_queue, queue_pointer)

    def bubble_up(self, priority_queue, pointer):
        """this recursive method is created to control if a child is lower than his parent and, if this is true, it swap
        of their position.(from the end of the queue to top)"""
        parentpointer = self.parent(pointer)
        if parentpointer == -1:
            return
        if priority_queue[pointer] < priority_queue[parentpointer]:
            self.swap(priority_queue, pointer, parentpointer)
            self.bubble_up(priority_queue, parentpointer)

    def swap(self,priority_queue, child, parent):
        """this method is created to swap a parent with his child"""
        tmp = priority_queue[parent]
        priority_queue[parent] = priority_queue[child]
        priority_queue[child] = tmp

    def bubble_down(self, priority_queue, root):
        """this recursive method is created to control if a child is lower than his parent and, if this is true, it swap
            of their position. (from the root to down)"""
        child = self.young_child(root)
        lenght_last = len(priority_queue)
        if child >= lenght_last:
            return

        min_index = root

        for pointer in xrange(0, 2):
            app_child = child + pointer
            if app_child < len(priority_queue):
                if priority_queue[min_index] > priority_queue[app_child]:
                    min_index = app_child
        if min_index != root:
            self.swap(priority_queue, min_index, root)
            self.bubble_down(priority_queue, min_index)

    def extract_min(self, priority_queue):
        """this method is created to extract a minimum member in a priority queue and recall a function
        called bubble down """
        if priority_queue is None:
            raise ValueError("Empty Array ")
        else:
            minimum_element = priority_queue[1]
            n = len(priority_queue)
            priority_queue[1] = priority_queue[n-1]
            del priority_queue[-1]
            self.bubble_down(priority_queue, 1)

        return minimum_element

    def heap_sort(self, array, n):
        """this method is created to sort a data structure, given a Heap"""
        self.make_heap(array, n)
        for pointer in xrange(0, n):
           array[pointer] = self.extract_min(self.priority_queue)

        return array

    def parent(self, pointer):
        """this method is created to return the parent, given his child"""
        if pointer == 1:
            return -1
        else:
            return pointer / 2

    def young_child(self, parent):
        """this method is created to return the first child, given his parent"""
        return 2 * parent

    def __str__(self):

        stringheap = str(self.priority_queue)
        return stringheap

    def __len__(self):
        count = 1
        length = len(self.priority_queue)
        while count < length-1:
            count +=1
        return count


if __name__ == '__main__':
    # n = 6
    # array = []
    # array = array + [5]
    # array = array + [10]
    # array = array + [17]
    # array = array + [70]
    # array = array + [12]
    # array = array + [19]
    n = 6
    array = []
    array = array + [99]
    array = array + [77]
    array = array + [44]
    array = array + [25]
    array = array + [1]
    array = array + [27]
    heap = Heap(n)
    print array
    heap = Heap(n)
    print heap
    # print heap.make_heap(array, n)
    # print len(heap)
    # print len
    print str(heap)
    # print heap.extract_min(heap.priority_queue)
    print(heap.heap_sort(array, n))