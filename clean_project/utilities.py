"""this file is used for writing all support methods
"""
import sys
import unicodedata

BOLD = '\033[1m'
END = '\033[0m'

# Dictionary of keys that identify punctuation
TABLE = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))


def load_punctuation():
    punctuation = ""
    for x in range(sys.maxunicode):
        if unicodedata.category(unichr(x)).startswith('P'):
            punctuation += (unichr(x).encode("utf-8"))
    return punctuation


def search(search_word, memory):
    """
    Print all the occurrence of a given word
    :param search_word: Word given to search
    :param memory: Dictionary of all the occurrence(line numbers) for all words(keys) in file
    :return: No matches if the word doesn't exist in file or a list of all the line number where the word occurs
    """
    # partial matching version
    # if search_word not in memory:
    #     return "No matches"
    # else:
    for keys in memory.keys():
        if keys.startswith(search_word):
            for occurrence in memory.get(keys):
                print BOLD + search_word + END + keys[search_word.__len__():] + " in lines --> " + str(occurrence)
    # return memory.get(search_word)
