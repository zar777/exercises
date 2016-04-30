import unittest

from heap import Heap


class HeapTest(unittest.TestCase):

    def test_heap_creation(self):
        n = 6
        array = []
        array = array + [99]
        array = array + [77]
        array = array + [44]
        array = array + [25]
        array = array + [1]
        array = array + [27]
        heap = Heap(n)
        self.assertIsNone(heap.priority_queue)
        heap.make_heap(array, n)
        self.assertFalse(heap.priority_queue == array)
        self.assertTrue(len(heap) == len(array))
        self.assertEqual(str(heap), "[0, 1, 25, 27, 99, 44, 77]")

    def test_heap_sort(self):
        n = 6
        array = []
        array = array + [99]
        array = array + [77]
        array = array + [44]
        array = array + [25]
        array = array + [1]
        array = array + [27]
        heap = Heap(n)
        self.assertIsNone(heap.priority_queue)
        heap.heap_sort(array, 6)
        self.assertFalse(heap.priority_queue == array)
        self.assertTrue(len(heap) == len(array))
        self.assertEqual(str(heap), "[1, 25, 27, 44, 77, 99]")
