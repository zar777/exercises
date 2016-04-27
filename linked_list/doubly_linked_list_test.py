import unittest

from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):



    def test_doubly_linked_list_creation(self):

        doubly_linked_list = DoublyLinkedList()
        # Assert the linked list is created.
        self.assertIsNotNone(doubly_linked_list)
        # Assert the head of the linked list is None -> empty linked list.
        self.assertIsNone(doubly_linked_list.head)



    def test_doubly_linked_list_empty(self):

        doubly_linked_list = DoublyLinkedList()
        self.assertTrue(doubly_linked_list.__len__() == 0)
        self.assertEqual(doubly_linked_list.head, None)




    def test_doubly_linked_list_append(self):

        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(25)
        self.assertIsNotNone(doubly_linked_list)
        self.assertTrue(doubly_linked_list.__len__() == 1)
        doubly_linked_list.append("Riccardo")
        self.assertTrue(doubly_linked_list.__len__() == 2)
        self.assertTrue(doubly_linked_list.head.item == 25)
        self.assertTrue(doubly_linked_list.tail.item == "Riccardo")
        self.assertEqual(doubly_linked_list.tail.next, None)
        self.assertTrue(doubly_linked_list.head.next.item == "Riccardo")
        self.assertFalse(doubly_linked_list.head.next.item == "25")
        doubly_linked_list.append("Try")
        self.assertTrue(doubly_linked_list.head.item == 25)
        self.assertTrue(doubly_linked_list.head.next.item == "Riccardo")
        self.assertTrue(doubly_linked_list.tail.item == "Try")
        self.assertTrue(doubly_linked_list.head.next.item == "Riccardo")
        self.assertEqual(doubly_linked_list.tail.next, None)



    def test_doubly_linked_list_insert(self):

        doubly_linked_list = DoublyLinkedList()
        with self.assertRaises(ValueError):
            doubly_linked_list.insert(99, 5)
        print doubly_linked_list.append(25)
        print doubly_linked_list.append("Riccardo")
        print doubly_linked_list.append("Try")
        print doubly_linked_list.insert(6, 3)
        self.assertTrue(doubly_linked_list.tail.previous.item == "Try")
        self.assertEqual(doubly_linked_list.tail.next, None)
        self.assertTrue(doubly_linked_list.tail.item == 6)




    def test_doubly_linked_list_insert_head(self):

        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_head(25)
        self.assertIsNotNone(doubly_linked_list)
        self.assertTrue(doubly_linked_list.__len__() == 1)
        doubly_linked_list.insert_head("Riccardo")
        self.assertTrue(doubly_linked_list.__len__() == 2)
        self.assertTrue(doubly_linked_list.head.item == "Riccardo")
        self.assertFalse(doubly_linked_list.head.next.item == "Riccardo")
        self.assertTrue(doubly_linked_list.head.next.item == 25)



    def test_doubly_linked_list_delete(self):

        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(25)
        doubly_linked_list.append("Riccardo")
        doubly_linked_list.append("Try")
        doubly_linked_list.insert(6, 3)
        self.assertIsNotNone(doubly_linked_list)
        self.assertTrue(doubly_linked_list.__len__() == 4)
        self.assertTrue(doubly_linked_list.tail.item == 6)
        doubly_linked_list.delete(3)
        self.assertTrue(doubly_linked_list.__len__() == 3)
        self.assertTrue(doubly_linked_list.tail.item == "Try")
        self.assertFalse(doubly_linked_list.tail.item == 6)
        self.assertTrue(doubly_linked_list.head.item == 25)
        self.assertFalse(doubly_linked_list.head.next.item == "Try")
        self.assertTrue(doubly_linked_list.head.next.item == "Riccardo")
        doubly_linked_list.delete(0)
        self.assertTrue(doubly_linked_list.head.item == "Riccardo")
        self.assertTrue(doubly_linked_list.head.next.item == "Try")




    def test_doubly_linked_list_search(self):

        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(25)
        pos = doubly_linked_list.search(25)
        self.assertIsNotNone(doubly_linked_list)
        self.assertTrue(pos == 0)
        doubly_linked_list.append("Riccardo")
        pos = doubly_linked_list.search("Riccardo")
        self.assertEqual(pos,1)
        doubly_linked_list.insert_head("Prova")
        pos = doubly_linked_list.search("Prova")
        self.assertTrue(pos == 0)



if __name__ == '__main__':
    unittest.main()
