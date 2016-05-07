from linked_list.linked_list import LinkedList, Node


class CircularLinkedList(LinkedList):
    """this class is created to represent a circular linked list"""
    def __init__(self):
        super(CircularLinkedList, self).__init__()

    def find_loop_element(self, dictionary):

        current = self.head

        while 1 != 0:
            if dictionary.get(current.item) is False:
                dictionary[current.item] = True
                return current.item
            if current.item not in dictionary:
                dictionary[current.item] = False

            current = current.next


if __name__ == '__main__':
    dictionary = {}
    circular_linked = CircularLinkedList()
    circular_linked.append("A")
    circular_linked.append("B")
    circular_linked.append("C")
    circular_linked.append("D")
    circular_linked.append("E")
    circular_linked.append("C")
    print circular_linked.find_loop_element(dictionary)
