"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import cmd

import search

BOLD = '\033[1m'
END = '\033[0m'


class Search(cmd.Cmd):

    def __init__(self, json_path):
        cmd.Cmd.__init__(self)
        self.json_path = json_path

    def do_search(self, search_word):
        """
        Print all the occurrence of a given word
        :param search_word: Word given to search
        """
        try:
            results = search.search(search_word, self.json_path)
            search.print_output(search_word, results)
        except IOError as e:
            print 'File or path not found: %s' % e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path')
    args = parser.parse_args()
    cmd_line = Search(args.json_path)
    cmd_line.cmdloop()
