"""
1. Add a method insert(item, pos) which will insert an item at position pos.
2. Add a method __len__() that returns the length of the linked list.
3. Add a method append(item) after you rename current append as insert_head(item)
4. Write tests for all the existing and new methods.
5. Write docstrings for each class and method.
"""
class LinkedList(object):
    """this class is created to represent a linked list and all usefull methods for clients"""

    def __init__(self):
        self.head = None



    def append(self, item):
        """given an item, this method append it at the end(tail) of linked-list"""
        current = self.head

        if self.head == None:
            node = Node(None, item)
            self.head = node

            return self
        while(current.next != None):
            current = current.next

        new_node = Node(None, item)
        current.next = new_node

        # TODO(gianluca): improve efficiently algorithm
        return self



    def insert(self,item_new, pos):
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
            raise ValueError("Invalid Position %d" %pos)

        previous_position.next = new_node
        new_node.next = current

        return self



    def insert_head(self, item):
        """given an item, this method append it at the beginning(head) of linked-list"""
        if self.head == None:
            node = Node(None, item)
            self.head = node

            return self
        new_node = Node(self.head,    item)
        self.head = new_node

        return self



    def delete(self, pos):
        """given a position, it delete the node selected and return the item deleted"""
        actual_position = 0
        previous_position = None
        current = self.head

        while actual_position != pos:

            previous_position = current
            current = current.next
            actual_position +=1
        if pos != 0:
            previous_position.next = current.next
        else:
            previous_position = current
            self.head = current.next
            return previous_position

        return current.item



    def search(self, item):
        """given an item, it search the i-th item and return the position"""
        position = 0
        current = self.head

        while current.item != item:

            position += 1
            current = current.next

        return position




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
            count +=1

        return count




class Node(object):
    """this class is created to represent a Node used for a linked-list"""
    def __init__(self, next_item, item):
        self.next = next_item
        self.item = item

    def __str__(self):
        stringNode = '[%s]' %self.item
        return stringNode




if __name__ == '__main__':

    linked_list = LinkedList()
    print linked_list.insert_head(5)
    print linked_list.__len__()
    print linked_list.insert_head(-1)
    print linked_list.__len__()
    print linked_list.insert_head('test')
    print linked_list.__len__()
    linked_list.insert_head(1)
    pos = linked_list.search(1)
    print linked_list.__len__()
    print pos
    print linked_list.__len__()
    print linked_list.delete(pos)
    print linked_list
    print linked_list.insert(6,1)
    print linked_list.__len__()
    print linked_list.append(25)
    print linked_list.__len__()
