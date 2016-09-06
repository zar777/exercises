"""Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Exercises 2.1
I haven't done a Follow up """

from collections import Counter
from linked_list.linked_list import LinkedList, Node



class RemoveDuplicates(LinkedList):
    def __init__(self):
        super(RemoveDuplicates, self).__init__()

    def remove(self):
        current = self.head
        buffer = []

        while current is not None:
            buffer.append(current.item)
            current = current.next

        dictionary = Counter(buffer)
        self.delete(dictionary)

        return self

    def delete(self, dictionary):
        """it delete the node selected(if duplicated) and return the item deleted"""
        actual_position = 0
        previous_position = None
        current = self.head

        while current is not None:
            dict_element = dictionary.get(current.item)
            if dict_element > 1:
                if current != self.head:
                    dictionary[current.item] = dict_element-1
                    previous_position.next = current.next
                else:
                    dictionary[current.item] = dict_element-1
                    self.head = current.next
            current = current.next
            actual_position += 1

        return dictionary

if __name__ == '__main__':

    duplicates = RemoveDuplicates()
    print duplicates.append(30)
    print duplicates.append(30)
    print duplicates.append(25)
    print duplicates.append(25)
    print duplicates.append(25)
    print duplicates.append(30)
    print len(duplicates)
    print duplicates.remove()
