class Stack(object):
    """this class is created to represent a Stack and all useFull methods for clients"""

    def __init__(self):
        self.head = None


    def push(self, element):
        """given an item, this method append it at the beginning(head) of the Stack"""
        if self.head is None:

            node = Node(None, element)
            self.head = node

            return self

        node = Node(self.head, element)
        self.head = node

        return self

    def pop(self):
        """it delete the node in head and return the item deleted"""
        if self.head is None:
            raise ValueError("No such Element")
        else:
            item = self.head.item
            self.head = self.head.next

        return item



    def __str__(self):

        string = ''
        current = self.head

        if current == None:
            return string

        while current != None:
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
    """this class is created to represent a Node used for a Stack"""
    def __init__(self, next_item, item):
        self.next = next_item
        self.item = item

    def __str__(self):
        stringnode = '[%s]' %self.item
        return stringnode




if __name__ == '__main__':

    stack = Stack()
    print stack
    print stack.__len__()
    stack.push(25)
    print stack
    print stack.__len__()
    print stack.push("Riccardo")
    print stack.__len__()
    print stack.pop()
    print stack.__len__()
    print stack
    print stack.pop()
    print stack.__len__()
    print stack.pop()
