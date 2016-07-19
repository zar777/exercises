"""
SearchCli a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import cmd

import search_engine

BOLD = '\033[1m'
END = '\033[0m'


def print_output(search_word, results):
    """
    Print output of search
    :param search_word: Word given to search
    :param results: list of tuples(filename, occurrence in a given file)
    """
    if results:
        print "{bold} {word} {end} is contained in the following file/lines:" \
            .format(bold=BOLD, word=search_word, end=END)
        for word, filename, occurrence in results:
            print "--> %s: %s" % (filename, str(occurrence).strip("[]"))
    else:
        print "No matches"


class SearchCli(cmd.Cmd):

    def __init__(self, engine):
        cmd.Cmd.__init__(self)
        self.engine = engine

    def do_search(self, search_word):
        """
        Print all the occurrence of a given word
        :param search_word: Word given to search
        """
        try:
            results = self.engine.search(search_word)
            print_output(search_word, results)
        except IOError as e:
            print 'File or path not found: %s' % e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-word', default="", help='The word to search for')
    parser.add_argument('--db_config', required=True, help='Path of file used for database connection')
    parser.add_argument('--cli', default=False, help='If True, enable CLI mode')
    args = parser.parse_args()
    engine = search_engine.SearchEngine(args.db_config)
    if args.cli:
        SearchCli(engine).cmdloop()
    else:
        results = engine.search(args.word)
        print_output(args.word, results)
