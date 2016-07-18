import collections
import unittest

import psycopg2

import clean_project.project.index


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
        self.assertRaises(ValueError, clean_project.project.index.index,
                          'data/config_empty_file.yaml')

    def test_full_dictionary(self):
        index_object = clean_project.project.index.index('data/config_file.yaml')
        result_converted = convert(index_object)
        self.assertEqual({'ago': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'and': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'from': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [1]},
                          'favourite': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'tre': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'university': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'programming': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'years': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'languages': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'python': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'computer': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [1]},
                          'come': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [1]},
                          'at': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'roma': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'graduated': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [2]},
                          'java': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'engineer': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [1]},
                          'my': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]},
                          'rome': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [1]},
                          'are': {'https://s3.amazonaws.com/dirtyfiles/background.txt': [3]}}, result_converted)

    def test_file_not_exist(self):
        self.assertRaises(IOError, clean_project.project.index.index, "/path/file_not_exist")

    def test_index_database(self):
        index_object = clean_project.project.index.index('data/config_file.yaml')
        clean_project.project.index.build_index(index_object, 'data/config.cfg')
        db_keys = clean_project.project.index.load_config_file('data/config.cfg')
        connection = psycopg2.connect(database=db_keys.get('database'),
                                      user=db_keys.get('user'),
                                      password=db_keys.get('password'),
                                      host=db_keys.get('host'),
                                      port=db_keys.get('port'),
                                      sslmode=db_keys.get('sslmode'))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM index where file = 'https://s3.amazonaws.com/dirtyfiles/background.txt'"
                       " order by 1;")
        table_content = cursor.fetchall()
        self.assertEqual([('ago', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('and', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('are', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('at', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('come', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [1]),
                          ('computer', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [1]),
                          ('engineer', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [1]),
                          ('favourite', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('from', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [1]),
                          ('graduated', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('java', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('languages', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('my', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('programming', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('python', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [3]),
                          ('roma', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('rome', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [1]),
                          ('tre', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('university', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2]),
                          ('years', 'https://s3.amazonaws.com/dirtyfiles/background.txt', [2])], table_content)



