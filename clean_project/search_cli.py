"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import cmd

import search

BOLD = '\033[1m'
END = '\033[0m'


class SearchCli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

    def do_search(self, search_word):
        """
        Print all the occurrence of a given word
        :param search_word: Word given to search
        """
        try:
            results = search.search(search_word)
            search.print_output(search_word, results)
        except IOError as e:
            print 'File or path not found: %s' % e


if __name__ == '__main__':
    SearchCli().cmdloop()
