import unittest

from queue import Queue


class QueueTest(unittest.TestCase):



    def test_queue_creation(self):
        queue = Queue()
        # Assert the linked list is created.
        self.assertIsNotNone(queue)
        # Assert the head of the linked list is None -> empty linked list.
        self.assertIsNone(queue.head)



    def test_queue_empty(self):
        queue = Queue()
        self.assertTrue(queue.__len__() == 0)
        self.assertEqual(queue.head, None)



    def test_queue_enqueue(self):
        queue = Queue()
        queue.enqueue(25)
        self.assertIsNotNone(queue)
        self.assertTrue(queue.__len__() == 1)
        queue.enqueue("Riccardo")
        self.assertTrue(queue.__len__() == 2)
        self.assertTrue(queue.head.item == 25)
        self.assertFalse(queue.head.next.item == 25)
        self.assertTrue(queue.head.next.item == "Riccardo")



    def test_queue_dequeue(self):
        queue = Queue()
        queue.enqueue(25)
        queue.enqueue("Riccardo")
        queue.enqueue("Try")
        self.assertIsNotNone(queue)
        self.assertTrue(queue.__len__() == 3)
        queue.dequeue()
        self.assertTrue(queue.__len__() == 2)
        self.assertTrue(queue.head.item == "Riccardo")
        self.assertFalse(queue.head.next.item == 25)
        self.assertTrue(queue.head.next.item == "Try")
        queue.dequeue()
        self.assertTrue(queue.head.item == "Try")
        self.assertTrue(queue.head.next is None)
        item = queue.dequeue()
        self.assertTrue(item == "Try")
        self.assertTrue(queue.head is None)


if __name__ == '__main__':
    unittest.main()
