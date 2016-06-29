import argparse
from index import load_config_file
import psycopg2
import search_cli


class SearchEngine(object):
    def __init__(self, connect_path):
        self.connect_path = connect_path

    def search(self, search_word):
        """
        Search if a given word is in bucket of files
        :param search_word: Word given to search
        :return: List of tuples composed by the given word, file and all the occurrences found
        """
        result_search = []
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(database=load_config_file(self.connect_path).get('database'),
                                          user=load_config_file(self.connect_path).get('user'),
                                          password=load_config_file(self.connect_path).get('password'))
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM index WHERE word = '%s';" % search_word)
            result_search = cursor.fetchall()
        except psycopg2.DataError, e:
            print 'Data error detected: %s' % e
        finally:
            if connection:
                cursor.close()
                connection.close()
        return result_search

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('connect_path')
    args = parser.parse_args()
    try:
        results = SearchEngine(args.connect_path).search(args.word)
        search_cli.Search(args.connect_path).print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e