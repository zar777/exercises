"""
Create a JSON file used to indexing all words in a config_file.yaml
"""
import argparse
import codecs
import json
import os
import yaml

from collections import defaultdict
import clean_file


def index(config_path, index_path):
    """
    Build a dictionary, given a configuration files
    :param config_path: Configuration path which contains a list of files that will be cleaned
    :param index_path: Path of index file
    :return: Index file
    """
    with open(config_path) as config_file:
        data = yaml.load(config_file)
    if data is not None:
        key_index = lambda: defaultdict(list)
        index_words = defaultdict(key_index)
        for file_dirty in data['files_path']:
            with codecs.open(file_dirty.get('file'), 'r', 'utf-8') as source_file:
                # Used 1-based indexing for showing line numbers in output representation
                for i, line in enumerate(source_file, 1):
                    cleaned_line = clean_file.sanitize(line)
                    for word in cleaned_line.split():
                        index_words[word.lower()][source_file.name].append(i)
    else:
        raise ValueError('Empty configuration file')
    with open(index_path, 'w') as index_file:
        json.dump(index_words, index_file, sort_keys=True, indent=4)
    return index_words


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path')
    parser.add_argument('--index', type=str, default=os.getcwd() + "/index.json")
    args = parser.parse_args()
    try:
        index(args.config_path, args.index)
    except IOError as e:
        print 'File or path not found: %s' % e
