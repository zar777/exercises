import unittest

import clean_project.project.index
import clean_project.project.search_engine


class SearchTest(unittest.TestCase):

    def test_no_match(self):
            clean_project.project.index.index('data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("wrongword"))

    def test_match(self):
            clean_project.project.index.index('data/config_file.yaml')
            self.assertEqual([('bulgaria', 'test.txt', [1, 2, 4]),
                              ('bulgaria', 'https://s3.amazonaws.com/dirtyfiles/news', [38, 38, 415])],
                             clean_project.project.search_engine.SearchEngine('data/config.cfg').search("bulgaria"))

    def test_no_match_single_character(self):
            clean_project.project.index.index('data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("a"))

    def test_no_match_punctuation(self):
            clean_project.project.index.index('data/config_file.yaml')
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("-more_videos:!"))
