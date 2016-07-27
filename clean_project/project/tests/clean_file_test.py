# -*- coding: utf-8 -*-
import tempfile
import unittest

from clean_project.project.clean_file import clean_up, sanitize


class CleanFileTest(unittest.TestCase):

    def test_punctuation_double_quotes_character(self):
        string_test = u'hi e a“”how are "you". a'
        self.assertEqual('hi     how are  you   ', sanitize(string_test))

    def test_punctuation_hyphen_character(self):
        string_test = u"hi e‐‑‒–a how are--- you. a"
        self.assertEqual('hi     how are  you   ', sanitize(string_test))

    def test_punctuation_underscore_character(self):
        string_test = u"hi e＿a how_are_you.＿a"
        self.assertEqual('hi     how are you  ', sanitize(string_test))

    def test_punctuation_apostrophe_character(self):
        string_test = u"hi e a‘’how' are' you. a"
        self.assertEqual('hi     how  are  you   ', sanitize(string_test))

    def test_punctuation_single_character(self):
        string_test = u"hi e a how are you. a"
        self.assertEqual("hi     how are you   ", sanitize(string_test))

    def test_punctuation_begin_sentence(self):
        string_test = u"-»¿;hi how are you."
        self.assertEqual(" hi how are you ", sanitize(string_test))

    def test_punctuation_end_sentence(self):
        string_test = u"hi how are you???»¿;"
        self.assertEqual("hi how are you ", sanitize(string_test))

    def test_punctuation_middle_sentence(self):
        string_test = u"hi, how,»¿; are, you"
        self.assertEqual("hi  how  are  you", sanitize(string_test))

    def test_punctuation_shuffle_sentence(self):
        string_test = u"hi, 'anti,»¿;-bribery! you:?"
        self.assertEqual("hi   anti bribery  you ", sanitize(string_test))

    def test_punctuation_parenthesis_sentence(self):
        string_test = u"({hi} [anti-bribery] /you)"
        self.assertEqual(" hi   anti bribery   you ", sanitize(string_test))

    def test_punctuation_hyphen_sentence(self):
        string_test = u"gianluca_parente@gmail com!!!"
        self.assertEqual("gianluca parente gmail com ", sanitize(string_test))

    def test_all_punctuation_in_empty_file(self):
        with tempfile.NamedTemporaryFile() as src_file:
            with tempfile.NamedTemporaryFile() as dst_file:
                input_file = src_file.read()
                clean_up(src_file.name, dst_file.name)
                output_file = dst_file.read()
                self.assertEqual(input_file, output_file)

    def test_all_punctuation_in_file(self):
        with tempfile.NamedTemporaryFile() as dst_file:
            clean_up("data/punctuation.txt", dst_file.name)
            output_file = dst_file.read()
            self.assertEqual("   ", output_file)

    def test_all_punctuation_not_existing_source_file(self):
            with tempfile.NamedTemporaryFile() as dst_file:
                self.assertRaises(IOError, clean_up, "/path/file_not_exist", dst_file.name)

    def test_all_punctuation_not_existing_dest_file(self):
        with tempfile.NamedTemporaryFile() as src_file:
            self.assertRaises(IOError, clean_up, src_file.name, "/path/file_not_exist")
