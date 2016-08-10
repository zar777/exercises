import unittest

from making_pairs import MakingPairs


class MakingPairsTest(unittest.TestCase):

    def setUp(self):
        self.making_pairs = MakingPairs()

    def test_complex(self):
        cards_complex = [43, 23, 10, 39, 39, 22, 22, 0, 3, 4, 3, 2]
        self.assertEqual(102, self.making_pairs.get(cards_complex))

    def test_simple(self):
        cards_single = [5]
        self.assertEqual(2, self.making_pairs.get(cards_single))
        cards_zero = [0]
        self.assertEqual(0, self.making_pairs.get(cards_zero))
        cards_ones = [1, 1, 1]
        self.assertEqual(0, self.making_pairs.get(cards_ones))
        cards_two = [2, 2, 2]
        self.assertEqual(3, self.making_pairs.get(cards_two))
