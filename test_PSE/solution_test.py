import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertEqual(self.solution.solution(), "")

    def test_one(self):
        self.assertEqual(self.solution.solution(), "")

    def test_odd(self):
        self.assertEqual(self.solution.solution(), "")

    def test_even(self):
        self.assertEqual(self.solution.solution(), "")