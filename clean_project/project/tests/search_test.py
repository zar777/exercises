import unittest

import clean_project.project.index
import clean_project.project.search_engine


class SearchTest(unittest.TestCase):

    def test_no_match(self):
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("wrongword"))

    def test_match(self):
            self.assertEqual([('bulgaria bush sign', 'test.txt', [1, 2])],
                             clean_project.project.search_engine.SearchEngine('data/config.cfg')
                             .search("bulgaria bush sign"))

    def test_no_match_single_character(self):
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("a"))

    def test_no_match_punctuation(self):
            self.assertEqual([], clean_project.project.search_engine.SearchEngine('data/config.cfg').search("-more_videos:!"))
