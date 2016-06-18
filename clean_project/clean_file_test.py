# -*- coding: utf-8 -*-
import tempfile
import unittest


from clean_file import clean_up, sanitize


class CleanFileTest(unittest.TestCase):

    def test_punctuation_begin_sentence(self):
        string_test = u"-»¿;hi how are you"
        self.assertEqual("-hi how are you", sanitize(string_test))

    def test_punctuation_end_sentence(self):
        string_test = u"hi how are you???»¿;"
        self.assertEqual("hi how are you", sanitize(string_test))

    def test_punctuation_middle_sentence(self):
        string_test = u"hi, how,»¿; are, you"
        self.assertEqual("hi how are you", sanitize(string_test))

    def test_punctuation_hyphen_sentence(self):
        string_test = u"gianluca_parente@gmail.com?????????"
        self.assertEqual("gianluca_parente@gmail.com", sanitize(string_test))

    def test_all_punctuation_in_empty_file(self):
        with tempfile.NamedTemporaryFile() as src_file:
            with tempfile.NamedTemporaryFile() as dst_file:
                input_file = src_file.read()
                clean_up(src_file.name, dst_file.name)
                output_file = dst_file.read()
                self.assertEqual(input_file, output_file)

    def test_all_punctuation_in_file(self):
        with tempfile.NamedTemporaryFile() as dst_file:
            clean_up("test_data/punctuation.txt", dst_file.name)
            output_file = dst_file.read()
            self.assertEqual("'-.@_", output_file)

    def test_all_punctuation_not_existing_file(self):
            with tempfile.NamedTemporaryFile() as dst_file:
                self.assertRaises(IOError, clean_up, "/path/file_not_exist", dst_file.name)
