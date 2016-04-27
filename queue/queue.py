class Queue(object):
    """this class is created to represent a Queue and all useFull methods for clients"""

    def __init__(self):
        self.head = None


    def enqueue(self, element):
        """given an item, this method append it at the beginning(head) of the Queue"""
        current = self.head

        if self.head is None:

            node = Node(None, element)
            self.head = node

            return self

        while current.next is not None:

            current = current.next

        node = Node(None, element)
        current.next = node

        return self

    def dequeue(self):
        """it delete the node in tail and return the item deleted"""
        if self.head is None:
            raise ValueError("No such Element")
        else:
            item = self.head.item
            self.head = self.head.next

        return item



    def __str__(self):

        string = ''
        current = self.head

        if current is None:
            return string

        while current is not None:
            string += str(current)
            current = current.next

        return string



    def __len__(self):

        count = 1
        current = self.head
        if self.head is None:
            count = 0
            return count
        while current.next is not None:

            current = current.next
            count += 1

        return count




class Node(object):
    """this class is created to represent a Node used for a Queue"""
    def __init__(self, next_item, item):
        self.next = next_item
        self.item = item

    def __str__(self):
        stringnode = '[%s]' % self.item
        return stringnode




if __name__ == '__main__':

    queue = Queue()
    print queue
    print queue.__len__()
    queue.enqueue(25)
    print queue
    print queue.__len__()
    print queue.enqueue("Riccardo")
    print queue.__len__()
    print queue.enqueue("Ciao")
    print queue.__len__()
    print queue.enqueue(999)
    print queue.__len__()
    print queue.dequeue()
    print queue.__len__()
    print queue
    print queue.dequeue()
    print queue.__len__()
    print queue
    print queue.dequeue()
    print queue.__len__()
    print queue
    print queue.dequeue()
    print queue.__len__()
    print queue
