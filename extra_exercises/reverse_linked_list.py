"""Print a linked list in reverse order. Follow-up: try to do it without additional memory (simple variables are fine)."""
from linked_list.linked_list import LinkedList


def reverse_with_list(linked_list):
    reverse_linked = []
    current = linked_list.head
    while current.next is not None:
        reverse_linked.insert(0, current.item)
        current = current.next
    reverse_linked.insert(0, current.item)
    return reverse_linked


def reverse_with_variables(linked_list):
    """follow up fallito"""
    current = linked_list.head
    head_item = current.item
    while current.next is not None:
        head_provisional = linked_list.delete(current.next.item)
        linked_list.insert_head(head_provisional)
    return linked_list


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(9)
    linked_list.append(5)
    linked_list.append(15)
    linked_list.append(2)
    print linked_list
    #print reverse_with_list(linked_list)
    print reverse_with_variables(linked_list)
