"""
Search a word in a file and return all the occurrences specified the line numbers
"""
import argparse
import psycopg2

from index import load_config_file

BOLD = '\033[1m'
END = '\033[0m'


class Search(object):
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

    def print_output(self, search_word, results):
        """
        Print output of search
        :param search_word: Word given to search
        :param results: list of tuples(filename, occurrence in a given file)
        """
        if results:
            print "The word {bold} {word} {end} is contained in the following file/lines:" \
                .format(bold=BOLD, word=search_word, end=END)
            for word, filename, occurrence in results:
                print "--> %s: %s" % (filename, str(occurrence).strip("[]"))
        else:
            print "No matches"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('connect_path')
    args = parser.parse_args()
    try:
        results = Search(args.connect_path).search(args.word)
        Search(args.connect_path).print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e
