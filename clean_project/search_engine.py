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
        database = load_config_file(self.connect_path).get('database')
        user = load_config_file(self.connect_path).get('user')
        password = load_config_file(self.connect_path).get('password')
        connection = psycopg2.connect(database=database, user=user, password=password)
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM index WHERE word = '%s';" % search_word)
                    result_search = cursor.fetchall()
        finally:
            connection.close()
        return result_search

if __name__ == '__main__':
    pass
