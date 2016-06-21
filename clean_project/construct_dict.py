# -*- coding: utf-8 -*-
"""
Construct a JSON file used to indexing all words in a config_file.yaml
"""
import argparse
import codecs
import json
import yaml

from collections import defaultdict
from clean_file import sanitize


def construct_dictionary(yaml_path, path_json_file):
    """
    Construct the dictionary, given a configuration files
    :param yaml_path: Yaml's path that contains a list of files that will be cleaned
    :param path_json_file: Path of JSON file (indexing)
    :return: JSON File
    """
    output = []
    with open(yaml_path) as config_file:
        data = yaml.load(config_file)
        for file_dirty in data['files_path']:
            with codecs.open(file_dirty, 'r', 'utf-8') as source_file:
                memory = defaultdict(list)
                memory["file_name"].append(file_dirty)
                for i, line in enumerate(source_file, 1):
                    cleaned_line = sanitize(line)
                    for word in cleaned_line.split():
                        memory[word.lower()].append(i)
            output.append(memory)
    with open(path_json_file, 'w') as json_file:
        json.dump(output, json_file, sort_keys=True, indent=4)
    return json_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml_path')
    parser.add_argument('json_path')
    args = parser.parse_args()
    try:
        construct_dictionary(args.yaml_path, args.json_path)
    except IOError as e:
        print 'File or path not found: %s' % e