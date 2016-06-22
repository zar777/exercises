# -*- coding: utf-8 -*-
"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import cmd
import json

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
        :return: List of dict used for indexing words
        """
        try:
            with open(self.json_path) as json_file:
                list_of_dict = json.load(json_file)
                count_match = 0
                for file_dict in list_of_dict:
                    if search_word in file_dict:
                        count_match += 1
                        print "The word " + BOLD + search_word + END + " is contains in the following file/lines:"
                        for occurrence in file_dict.get(search_word):
                            file_name = file_dict.get('file_name')[0].split('/')
                            print "--> " + file_name[len(file_name) - 1] + ': ' + str(occurrence)
                if count_match == 0:
                    print "No matches"
            # return feeds.get(search_word)
        except IOError as e:
            print 'File or path not found: %s' % e

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('word')
    parser.add_argument('json_path')
    args = parser.parse_args()
    Search(args.json_path).cmdloop()
