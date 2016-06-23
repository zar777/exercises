import json
import tempfile
import unittest

import index


class ConstructDictTest(unittest.TestCase):

    def test_empty_yaml_file(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            self.assertEqual("Empty config file", index.index('test_data/config_empty_file.yaml', index_file.name))

    def test_full_dictionary(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            result = json.load(index_file)
            self.assertEqual({u'the': {u'test_data/full_file_dirty.txt': [1]},
                              u'as': {u'test_data/full_file_dirty.txt': [1, 2]},
                              u'bush': {u'test_data/full_file_dirty.txt': [1]},
                              u'bulgaria': {u'test_data/full_file_dirty.txt': [1, 3]}}, result)

    def test_file_not_exist(self):
        self.assertRaises(IOError, index.index, "/path/file_not_exist", '/path/index_file.json')



