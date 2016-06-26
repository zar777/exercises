"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import psycopg2

BOLD = '\033[1m'
END = '\033[0m'


def search(search_word):
    """
    Search if a given word is in bucket of files
    :param search_word: Word given to search
    :return: List of files and numbers of file when search_word occurrence
    """
    connection = None
    result_search = []
    try:
        connection = psycopg2.connect(database='index_db', user='gianluca', password='password')
        cursor = connection.cursor()
        # query = "SELECT * FROM index WHERE word = %s;" % search_word
        # data = search_word
        cursor.execute("SELECT * FROM index WHERE word = '%s';" % search_word)
        result_search = cursor.fetchall()

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e

    finally:

        if connection:
            connection.close()
        return result_search


def print_output(search_word, results):
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
        results = search(args.word)
        print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e
