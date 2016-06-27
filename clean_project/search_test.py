import unittest

import index
from search import Search


class SearchTest(unittest.TestCase):

    def test_no_match(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], Search('test_data/config.ini').search("wrongword"))

    def test_match(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([('bulgaria', 'home/test/news.txt', [22, 99, 44]),
                              ('bulgaria', 'test_data/full_file_dirty.txt', [1, 3])],
                             Search('test_data/config.ini').search("bulgaria"))

    def test_no_match_single_character(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], Search('test_data/config.ini').search("a"))

    def test_no_match_punctuation(self):
            index.index('test_data/config_file.yaml')
            self.assertEqual([], Search('test_data/config.ini').search("-more_videos:!"))
