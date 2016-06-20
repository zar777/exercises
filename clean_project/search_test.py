# -*- coding: utf-8 -*-
import unittest

from search import construct_dictionary, search


class SearchTest(unittest.TestCase):

    def test_empty_dictionary(self):
        self.assertEqual(0, construct_dictionary("test_data/empty_file.txt").keys().__len__())

    def test_full_dictionary(self):
        self.assertEqual(8, construct_dictionary("test_data/full_file_dirty.txt").keys().__len__())

    def test_file_not_exist(self):
        self.assertRaises(IOError, construct_dictionary, "/path/file_not_exist")

    def test_no_match(self):
        self.assertEqual("No matches", search("fake_word", construct_dictionary("test_data/full_file_dirty.txt")))

    def test_match(self):
        self.assertEqual([1, 3], search("bulgaria", construct_dictionary("test_data/full_file_dirty.txt")))

    def test_no_match_single_character(self):
        self.assertEqual("No matches", search("s", construct_dictionary("test_data/full_file_dirty.txt")))

    def test_no_match_punctuation(self):
        self.assertEqual("No matches", search("'", construct_dictionary("test_data/full_file_dirty.txt")))

