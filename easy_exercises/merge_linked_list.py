linked1: -1 -> 2 -> 4 -> 6

linked2: 0 -> 3 -> 4 -> 5

-1 -> 0 ->2 -> 3 -> 4 -> 4 -> 5 -> 6

class linked_list(object):
        def __init__(self, node):
            self.head = node

class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def solve(list1, list2):
    current_l1 = list1.head
    current_l2 = list2.head
    node = node(None)
    linked_l3 = linked_list(node)

    if current_l1 < current_l2:
                list3.head = current_l1
                current_l1.next = current_l2
    else:
                list3.head = current_l2
                current_l2.next = current_l1

    current_l3 = list.head

    while current_l1.next is not None and current_l2.next is not None:
             if current_l1 < current_l2:
                 current_l3.next = current_l1
                current_l1 = current_l1.next
            else:
                list3.head = current_l2
                current_l2.next = current_l1

