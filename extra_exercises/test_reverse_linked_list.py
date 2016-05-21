import unittest
from linked_list.linked_list import LinkedList
from reverse_linked_list import reverse_with_list

class ReverseLinkedListTest(unittest.TestCase):

    def test_reverse_linked_list_with_list(self):
        linked_list = LinkedList()
        linked_list.append(9)
        linked_list.append(5)
        linked_list.append(15)
        linked_list.append(2)
        self.assertIsNotNone(linked_list)
        self.assertEqual(linked_list.__str__(), '[9][5][15][2]')
        self.assertEqual(reverse_with_list(linked_list).__str__(), '[2, 15, 5, 9]')

    def test_reverse_linked_list_with_list(self):
        linked_list = LinkedList()
        linked_list.append(9)
        linked_list.append(5)
        linked_list.append(15)
        linked_list.append(2)
        self.assertIsNotNone(linked_list)
        self.assertEqual(linked_list.__str__(), '[9][5][15][2]')
        self.assertEqual(reverse_with_variables(linked_list).__str__(), '[2, 15, 5, 9]')