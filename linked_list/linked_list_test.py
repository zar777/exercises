import unittest

from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):



    def test_linked_list_creation(self):
        linked_list = LinkedList()
        # Assert the linked list is created.
        self.assertIsNotNone(linked_list)
        # Assert the head of the linked list is None -> empty linked list.
        self.assertIsNone(linked_list.head)



    def test_linked_list_empty(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.__len__()==0)
        self.assertEqual(linked_list.head, None)




    def test_linked_list_append(self):
        linked_list = LinkedList()
        linked_list.append(25)
        self.assertIsNotNone(linked_list)
        self.assertTrue(linked_list.__len__()==1)
        linked_list.append("Riccardo")
        self.assertTrue(linked_list.__len__()==2)
        self.assertTrue(linked_list.head.item==25)
        self.assertTrue(linked_list.head.next.item =="Riccardo")
        self.assertFalse(linked_list.head.next.item == "25")



    def test_linked_list_insert(self):
        linked_list = LinkedList()
        with self.assertRaises(ValueError):
            linked_list.insert(99, 5)




    def test_linked_list_insert_head(self):
        linked_list = LinkedList()
        linked_list.insert_head(25)
        self.assertIsNotNone(linked_list)
        self.assertTrue(linked_list.__len__() == 1)
        linked_list.insert_head("Riccardo")
        self.assertTrue(linked_list.__len__() == 2)
        self.assertTrue(linked_list.head.item == "Riccardo")
        self.assertFalse(linked_list.head.next.item == "Riccardo")
        self.assertTrue(linked_list.head.next.item == 25)



    # def test_linked_list_delete(self):
    #     SOLO DA TESTARE
    #     linked_list = LinkedList()()
    #     linked_list.append(25)
    #     linked_list.append("Riccardo")
    #     linked_list.append("Try")
    #     linked_list.insert(6, 3)
    #     self.assertIsNotNone(linked_list)
    #     self.assertTrue(linked_list.__len__() == 4)
    #     self.assertTrue(linked_list.tail.item == 6)
    #     linked_list.delete(3)
    #     self.assertTrue(linked_list.__len__() == 3)
    #     self.assertTrue(linked_list.tail.item == "Try")
    #     self.assertFalse(linked_list.tail.item == 6)
    #     self.assertTrue(linked_list.head.item == 25)
    #     self.assertFalse(linked_list.head.next.item == "Try")
    #     self.assertTrue(linked_list.head.next.item == "Riccardo")



    def test_linked_list_search(self):
        linked_list = LinkedList()
        linked_list.append(25)
        pos = linked_list.search(25)
        self.assertIsNotNone(linked_list)
        self.assertTrue(pos == 0)
        linked_list.append("Riccardo")
        pos = linked_list.search("Riccardo")
        self.assertEqual(pos,1)
        linked_list.insert_head("Prova")
        pos = linked_list.search("Prova")
        self.assertTrue(pos == 0)



if __name__ == '__main__':
    unittest.main()
