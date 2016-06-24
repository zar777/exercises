"""
Search a word in a file and return all the occurrence specified the line numbers
"""
import argparse
import json

BOLD = '\033[1m'
END = '\033[0m'


def search(search_word, json_path):
    """
    Search if a given word is in bucket of files
    :param search_word: Word given to search
    :param json_path: Indexing file
    :return: List of files and numbers of file when search_word occurrence
    """
    with open(json_path) as json_file:
        index = json.load(json_file)
        result_list = []
        if search_word in index:
            result_list = index[search_word].items()
    return result_list


def print_output(search_word, results):
    """
    Print output of search
    :param search_word: Word given to search
    :param results: list of tuples(filename, occurrence in a given file)
    """
    print "The word {bold} {word} {end} is contained in the following file/lines:" \
        .format(bold=BOLD, word=search_word, end=END)
    if results:
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
        results = search(args.word, args.json_path)
        print results
        print_output(args.word, results)
    except IOError as e:
        print 'File or path not found: %s' % e