"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def SortedInsert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head
    top = head
    # print node.data
    # print head.data
    # print "fuori dal while"
    while head.data < node.data and head.next is not None:
        # print "entra nel while"
        head = head.next
    # print "uscito dal while "
    if head.prev is None:
        node.next = head
        head.prev = node
        top = node
    elif head.next is None:
        head.next = node
        node.prev = head
    else:
        greater = head.next
        node.prev = head
        node.next = greater
        greater.prev = node
        head.next = node
    return top


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    print linked_list.append(2)
    print linked_list.append(3)
    print linked_list.append(4)
    print linked_list.append(5)
    print SortedInsert(linked_list.head, 1)
