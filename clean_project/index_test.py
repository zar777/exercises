import collections
import index
import psycopg2
import unittest


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
        self.assertRaises(ValueError, index.index, 'test_data/config_empty_file.yaml')

    def test_full_dictionary(self):
        index_object = index.index('test_data/config_file.yaml')
        result_converted = convert(index_object)
        self.assertEqual({'the': {'test_data/full_file_dirty.txt': [1]},
                          'bush': {'test_data/full_file_dirty.txt': [1]},
                          'as': {'test_data/full_file_dirty.txt': [1, 2]},
                          'bulgaria': {'test_data/full_file_dirty.txt': [1, 3]}}, result_converted)

    def test_file_not_exist(self):
        self.assertRaises(IOError, index.index, "/path/file_not_exist")

    def test_index_database(self):
        index_object = index.index('test_data/config_file.yaml')
        index.build_index(index_object, 'test_data/config.cfg')
        db_keys = index.load_config_file('test_data/config.cfg')
        connection = psycopg2.connect(database=db_keys.get('database'),
                                      user=db_keys.get('user'),
                                      password=db_keys.get('password'))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM index order by 1,2;")
        table_content = cursor.fetchall()
        self.assertEqual([('as', 'test_data/full_file_dirty.txt', [1, 2]),
                          ('bulgaria', 'test_data/full_file_dirty.txt', [1, 3]),
                          ('bulgaria', 'try/try.txt', [22, 84, 99]),
                          ('bush', 'test_data/full_file_dirty.txt', [1]),
                          ('the', 'test_data/full_file_dirty.txt', [1])], table_content)



