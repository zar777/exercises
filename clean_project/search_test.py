import unittest

import search


class SearchTest(unittest.TestCase):

    def test_no_match(self):
        self.assertEqual("No matches", search.search("fake_word", ))

    def test_match(self):
        self.assertEqual([1, 3], search.search("bulgaria", ))

    def test_no_match_single_character(self):
        self.assertEqual("No matches", search.search("s", ))

    def test_no_match_punctuation(self):
        self.assertEqual("No matches", search.search("'", ))

