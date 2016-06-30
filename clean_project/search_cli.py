"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import cmd
import search_engine

BOLD = '\033[1m'
END = '\033[0m'


class Search(cmd.Cmd):

    def __init__(self, connect_path):
        cmd.Cmd.__init__(self)
        self.connect_path = connect_path

    def do_search(self, search_word):
        """
        Print all the occurrence of a given word
        :param search_word: Word given to search
        """
        try:
            results = search_engine.SearchEngine(self.connect_path).search(search_word)
            self.print_output(search_word, results)
        except IOError as e:
            print 'File or path not found: %s' % e

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
    parser.add_argument('-word', nargs='?', default="")
    parser.add_argument('connect_path')
    parser.add_argument('-cli', nargs='?', default=False)
    args = parser.parse_args()
    try:
        if args.cli:
            Search(args.connect_path).cmdloop()
        else:
            results = search_engine.SearchEngine(args.connect_path).search(args.word)
            Search(args.connect_path).print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e
