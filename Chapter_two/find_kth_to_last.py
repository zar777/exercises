"""Implement an algorithm to find the nth to last element of a singly linked list.
Exercises 2.2"""

from linked_list.linked_list import LinkedList, Node


class FindLast(LinkedList):
    def __init__(self):
        super(FindLast, self).__init__()

    def find_kth(self, nth):
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        nth = count - nth
        count = 0
        current = self.head
        if nth >= 0:
            while count != nth:
                count += 1
                current = current.next
        else:
            return None
        return current

if __name__ == '__main__':

    finder = FindLast()
    finder.append(3)
    finder.append(4)
    finder.append(25)
    finder.append("ciao")
    finder.append(" ")
    finder.append("riccardo")
    print finder
    print finder.find_kth(0)