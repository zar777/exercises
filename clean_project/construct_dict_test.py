# -*- coding: utf-8 -*-
import json
import tempfile
import unittest

from construct_dict import construct_dictionary


class ConstructDictTest(unittest.TestCase):

    def test_empty_yaml_file(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as json_file:
            self.assertEqual("Empty yaml file", construct_dictionary('test_data/config_empty_file.yaml', json_file.name))

    def test_full_dictionary(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as json_file:
            construct_dictionary('test_data/config_file.yaml', json_file.name)
            result = json.load(json_file)
            self.assertEqual({u'file_name': [u'test_data/full_file_dirty.txt'], u'as': [1, 2], u'the': [1],
                              u'bush': [1], u'bulgaria': [1, 3]}, result[0])

    def test_file_not_exist(self):
        self.assertRaises(IOError, construct_dictionary, "/path/file_not_exist", '/path/json_file.json')



