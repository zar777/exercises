import json
import tempfile
import unittest

import index
import search


class SearchTest(unittest.TestCase):

    def test_no_match(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            self.assertEqual([], search.search("wrongword", index_file.name))

    def test_match(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            self.assertEqual([(u'test_data/full_file_dirty.txt', [1, 3])],
                             search.search("bulgaria", index_file.name))

    def test_no_match_single_character(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            self.assertEqual([], search.search("a", index_file.name))

    def test_no_match_punctuation(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            self.assertEqual([], search.search("-more_video's:!", index_file.name))
