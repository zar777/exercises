import unittest
from linked_list.linked_list import LinkedList
from reverse_linked_list import reverse_with_list, reverse_with_variables

class ReverseLinkedListTest(unittest.TestCase):

    def test_reverse_linked_list_with_list_even_number_of_elements(self):
        linked_list = LinkedList()
        linked_list.append(9)
        linked_list.append(5)
        linked_list.append(15)
        linked_list.append(2)
        self.assertEqual(linked_list.__str__(), '[9][5][15][2]')
        self.assertEqual(reverse_with_list(linked_list), [2, 15, 5, 9])

    def test_reverse_linked_list_one_element(self):
        linked_list = LinkedList()
        linked_list.append(9)
        self.assertEqual(linked_list.__str__(), '[9]')
        self.assertEqual(reverse_with_list(linked_list), [9])

    def test_reverse_linked_list_two_elements(self):
        linked_list = LinkedList()
        linked_list.append(9)
        linked_list.append(5)
        self.assertEqual(linked_list.__str__(), '[9][5]')
        self.assertEqual(reverse_with_list(linked_list), [5, 9])

    def test_reverse_linked_list_empty(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.__str__(), '')
        self.assertEqual(reverse_with_list(linked_list), [])

    def test_reverse_linked_list_odd_numbers_of_elements(self):
        linked_list = LinkedList()
        linked_list.append(9)
        linked_list.append(5)
        linked_list.append(15)
        self.assertEqual(linked_list.__str__(), '[9][5][15]')
        self.assertEqual(reverse_with_list(linked_list), [15, 5, 9])


    # def test_reverse_linked_list_with_variables(self):
    #     linked_list = LinkedList()
    #     linked_list.append(9)
    #     linked_list.append(5)
    #     linked_list.append(15)
    #     linked_list.append(2)
    #     self.assertEqual(linked_list.__str__(), '[9][5][15][2]')
    #     self.assertEqual(reverse_with_variables(linked_list).__str__(), '[2, 15, 5, 9]')