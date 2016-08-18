from linked_list.linked_list import LinkedList


def Reverse(head):
    stack = []
    while head:
        stack.append(head)
        head = head.next
    top = stack.pop()
    current = top
    while stack:
        current.next = stack.pop()
        current = current.next
    current.next = None
    return top

if __name__ == '__main__':
    linked_list = LinkedList()
    print linked_list.insert_head(5)
    print linked_list.insert_head(4)
    print linked_list.insert_head(1)
    print linked_list.insert_head(2)
    print Reverse(linked_list.head)