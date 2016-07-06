import unittest

import clean_project.project.index
import clean_project.project.search_engine


class SearchTest(unittest.TestCase):

    def test_no_match(self):
            clean_project.project.index.index('test_data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('test_data/config.cfg').search("wrongword"))

    def test_match(self):
            clean_project.project.index.index('test_data/config_file.yaml')
            self.assertEqual([('bulgaria', 'try/try.txt', [22, 84, 99]),
                              ('bulgaria', 'test_data/full_file_dirty.txt', [1, 3])],
                             clean_project.project.search_engine.SearchEngine('test_data/config.cfg').search("bulgaria"))

    def test_no_match_single_character(self):
            clean_project.project.index.index('test_data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('test_data/config.cfg').search("a"))

    def test_no_match_punctuation(self):
            clean_project.project.index.index('test_data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('test_data/config.cfg').search("-more_videos:!"))
