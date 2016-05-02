from collections import Counter
from linked_list.linked_list import LinkedList, Node



class RemoveDuplicates(LinkedList):
    def __init__(self):
        super(RemoveDuplicates, self).__init__()

    def remove(self):
        dictionary = {}
        position = 0
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
                if actual_position != 0 and current != self.head:
                    dictionary[current.item] = dict_element-1
                    previous_position.next = current.next
                else:
                    dictionary[current.item] = dict_element-1
                    previous_position = current
                    self.head = current.next
            previous_position = current
            current = current.next
            actual_position += 1

        return dictionary

if __name__ == '__main__':

    duplicates = RemoveDuplicates()
    print duplicates.append(30)
    print duplicates.append(25)
    print duplicates.append(25)
    print duplicates.append(25)
    print duplicates.append(25)
    print duplicates.append(30)
    print len(duplicates)
    print duplicates.remove()
