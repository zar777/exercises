import unittest

from stack import Stack


class StackTest(unittest.TestCase):



    def test_stack_creation(self):
        stack = Stack()
        # Assert the linked list is created.
        self.assertIsNotNone(stack)
        # Assert the head of the linked list is None -> empty linked list.
        self.assertIsNone(stack.head)



    def test_stack_empty(self):
        stack = Stack()
        self.assertTrue(stack.__len__() == 0)
        self.assertEqual(stack.head, None)



    def test_stack_push(self):
        stack = Stack()
        stack.push(25)
        self.assertIsNotNone(stack)
        self.assertTrue(stack.__len__() == 1)
        stack.push("Riccardo")
        self.assertTrue(stack.__len__() == 2)
        self.assertTrue(stack.head.item == "Riccardo")
        self.assertFalse(stack.head.next.item == "Riccardo")
        self.assertTrue(stack.head.next.item == 25)



    def test_stack_pop(self):
        stack = Stack()
        stack.push(25)
        stack.push("Riccardo")
        stack.push("Try")
        self.assertIsNotNone(stack)
        self.assertTrue(stack.__len__() == 3)
        stack.pop()
        self.assertTrue(stack.__len__() == 2)
        self.assertTrue(stack.head.item == "Riccardo")
        self.assertFalse(stack.head.next.item == "Try")
        self.assertTrue(stack.head.next.item == 25)
        stack.pop()
        self.assertTrue(stack.head.item == 25)
        self.assertTrue(stack.head.next is None)
        self.assertTrue(stack.pop() == 25)
        self.assertTrue(stack.head is None)


if __name__ == '__main__':
    unittest.main()
