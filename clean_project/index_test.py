import json
import tempfile
import unittest

import index
import collections


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


class IndexTest(unittest.TestCase):

    def test_empty_yaml_file(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            self.assertRaises(ValueError, index.index, 'test_data/config_empty_file.yaml', index_file.name)

    def test_full_dictionary(self):
        with tempfile.NamedTemporaryFile(suffix="JSON") as index_file:
            index.index('test_data/config_file.yaml', index_file.name)
            result = json.load(index_file)
            result_converted = convert(result)
            self.assertEqual({'the': {'test_data/full_file_dirty.txt': [1]},
                              'bush': {'test_data/full_file_dirty.txt': [1]},
                              'as': {'test_data/full_file_dirty.txt': [1, 2]},
                              'bulgaria': {'test_data/full_file_dirty.txt': [1, 3]}}, result_converted)

    def test_file_not_exist(self):
        self.assertRaises(IOError, index.index, "/path/file_not_exist", '/path/index_file.json')



