# -*- coding: utf-8 -*-
"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import json

BOLD = '\033[1m'
END = '\033[0m'


def search(search_word, json_path):
    """
    Print all the occurrence of a given word
    :param search_word: Word given to search
    :param json_path: Indexing file
    """
    with open(json_path) as json_file:
        list_of_dict = json.load(json_file)
        count_match = 0
        for file_dict in list_of_dict:
            if search_word in file_dict:
                count_match += 1
                for occurrence in file_dict.get(search_word):
                    file_name = file_dict.get('file_name')[0].split('/')
                    print 'In File ' + file_name[len(file_name)-1] + ' the word ' + BOLD + search_word + END \
                          + " is in lines --> " + str(occurrence)
        if count_match == 0:
            print "No matches"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('json_path')
    args = parser.parse_args()
    try:
        search(args.word, args.json_path)
    except IOError as e:
        print 'File or path not found: %s' % e