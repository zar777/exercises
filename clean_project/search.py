"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import psycopg2

from index import load_config_file

BOLD = '\033[1m'
END = '\033[0m'


class Search(object):
    def __init__(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(database=load_config_file().get('database'),
                                               user=load_config_file().get('user'),
                                               password=load_config_file().get('password'))
            self.cursor = self.connection.cursor()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e

    def search(self, search_word):
        """
        Search if a given word is in bucket of files
        :param search_word: Word given to search
        :return: List of files and numbers of file when search_word occurrence
        """
        result_search = []
        try:

            self.cursor.execute("SELECT * FROM index WHERE word = '%s';" % search_word)
            result_search = self.cursor.fetchall()
        except psycopg2.DataError, e:
            print 'Data error detected: %s' % e
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
    args = parser.parse_args()
    try:
        results = Search().search(args.word)
        Search().print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e
