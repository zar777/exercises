from linked_list import LinkedList, Node


class DoublyLinkedList(LinkedList):

    def __init__(self):
        super(DoublyLinkedList, self).__init__()
        self.tail = None


    def append(self, item):
        """given an item, this method append it at the end(tail) of linked-list"""

        if self.head is None:
            node = Node(None, item)
            self.head = node
            self.tail = node

            return self

        new_node = Node(None, item)
        old_tail = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.tail.previous = old_tail

        return self

    def insert(self, item_new, pos):
        """given an item and a position, this method insert an item at the position required"""

        actual_position = 0
        previous_position = None
        current = self.head
        new_node = Node(None, item_new)

        while actual_position != pos and current is not None:
            previous_position = current
            current = current.next
            actual_position += 1

        if actual_position != pos:
            raise ValueError("Invalid Position %d" % pos)

        previous_position.next = new_node
        new_node.next = current
        new_node.previous = previous_position

        if current is None:
            self.tail = new_node
        else:
            current.previous = new_node

        return self



    def delete(self, pos):
        """given a position, it delete the node selected and return the item deleted"""
        actual_position = 0
        previous_position = None
        current = self.head

        while actual_position != pos:
            previous_position = current
            current = current.next
            actual_position += 1

        if pos != 0:

            previous_position.next = current.next

            if previous_position.next is None:

                self.tail = previous_position

        else:

            previous_position = current
            self.head = current.next
            return previous_position

        return current.item



class DoublyNode(Node):

    def __init__(self, previous_pointer):
        super(DoublyNode, self).__init__()
        self.previous = previous_pointer



if __name__ == '__main__':

    doubly_linked_list = DoublyLinkedList()
    print doubly_linked_list.append(25)
    print doubly_linked_list.__len__()
    print doubly_linked_list.append("Riccardo")
    print doubly_linked_list.__len__()
    print doubly_linked_list.append("Try")
    print doubly_linked_list.__len__()
    print doubly_linked_list.insert(6, 3)
    print doubly_linked_list.__len__()
    print doubly_linked_list.delete(3)
    print doubly_linked_list
    # print linked_list.insert_head(5)
    # print linked_list.__len__()
    # print linked_list.insert_head(-1)
    # print linked_list.__len__()
    # print linked_list.insert_head('test')
    # print linked_list.__len__()
    # linked_list.insert_head(1)
    # pos = linked_list.search(1)
    # print linked_list.__len__()

