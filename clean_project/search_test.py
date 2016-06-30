import unittest

import index
import search_engine


class SearchTest(unittest.TestCase):

    def test_no_match(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], search_engine.SearchEngine('test_data/config.cfg').search("wrongword"))

    def test_match(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([('bulgaria', 'try/try.txt', [22, 84, 99]),
                              ('bulgaria', 'test_data/full_file_dirty.txt', [1, 3])],
                             search_engine.SearchEngine('test_data/config.cfg').search("bulgaria"))

    def test_no_match_single_character(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], search_engine.SearchEngine('test_data/config.cfg').search("a"))

    def test_no_match_punctuation(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], search_engine.SearchEngine('test_data/config.cfg').search("-more_videos:!"))
