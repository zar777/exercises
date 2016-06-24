"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import cmd

from search import Search

BOLD = '\033[1m'
END = '\033[0m'


class SearchCli(cmd.Cmd):

    def __init__(self, search):
        cmd.Cmd.__init__(self)
        self.search = search

    def do_search(self, search_word):
        """
        Print all the occurrence of a given word
        :param search_word: Word given to search
        """
        try:
            results = search_class.search(search_word)
            search_class.print_output(search_word, results)
        except IOError as e:
            print 'File or path not found: %s' % e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path')
    args = parser.parse_args()
    search_class = Search(args.json_path)
    cmd_line = SearchCli(search_class)
    cmd_line.cmdloop()
