"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import codecs
import json
import tempfile

from collections import defaultdict
from clean_file import clean_up

BOLD = '\033[1m'
END = '\033[0m'


def construct_dictionary(file_path):
    """
    Construct the dictionary, given a file
    :param file_path: Path's file for constructing the dictionary
    :return: Dictionary created
    """
    sanitize_file = clean_up(file_path, tempfile.NamedTemporaryFile().name)
    with codecs.open(sanitize_file, 'r', 'utf-8') as source_file:
        memory = defaultdict(list)
        for i, line in enumerate(source_file, 1):
            for word in line.split():
                memory[word.lower()].append(i)
    return memory


def search(search_word, memory):
    """
    Print all the occurrence of a given word
    :param search_word: Word given to search
    :param memory: Dictionary of all the occurrence(line numbers) for all words(keys) in file
    :return: No matches if the word doesn't exist in file or a list of all the line number where the word occurs
    """
    if search_word in memory:
        for occurrence in memory.get(search_word):
            print BOLD + search_word + END + " in lines --> " + str(occurrence)
    else:
        return "No matches"
    return memory.get(search_word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    parser.add_argument('file_path')
    args = parser.parse_args()
    try:
        memory = construct_dictionary(args.file_path)
        with open('/home/gianluca/Desktop/data.json', 'w') as fp:
            json.dump(memory, fp, sort_keys=True, indent=4)
        search(args.word, memory)
    except IOError as e:
        print 'File or path not found: %s' % e