"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import json

BOLD = '\033[1m'
END = '\033[0m'


class Search(object):
    def __init__(self, json_path):
        with open(json_path) as json_file:
            self.index = json.load(json_file)

    def search(self, search_word):
        """
        Search if a given word is in bucket of files
        :param search_word: Word given to search
        :return: List of files and numbers of file when search_word occurrence
        """
        if search_word in self.index:
            return self.index.get(search_word, {}).items()

    def print_output(self, search_word, results):
        """
        Print output of search
        :param search_word: Word given to search
        :param results: list of tuples(filename, occurrence in a given file)
        """
        if results:
            print "The word {bold} {word} {end} is contained in the following file/lines:" \
                .format(bold=BOLD, word=search_word, end=END)
            for filename, occurrence in results:
                    print "--> %s: %s" % (filename, str(occurrence).strip("[]"))
        else:
            print "No matches"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('json_path')
    args = parser.parse_args()
    try:
        search_object = Search(args.json_path)
        results = search_object.search(args.word)
        search_object.print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e
