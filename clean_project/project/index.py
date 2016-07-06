"""
Create a JSON file used to indexing all words in a config_file.yaml
"""
import argparse
import contextlib
import urllib
from ConfigParser import SafeConfigParser
from collections import defaultdict

import psycopg2
import yaml

import clean_file

# Update index table only if word and file match. Else do nothing
query_update = "UPDATE index SET occurrences=%s WHERE word=%s AND file=%s;"
# Insert word and file which exist in index table.
query_insert = ("INSERT INTO index (word, file, occurrences)"
                "VALUES (%s, %s, %s);")
# Select to verify if a key (word, file) exists
query_select = "SELECT 1 FROM index WHERE word=%s AND file=%s"


def load_config_file(connect_path):
    config = SafeConfigParser()
    config.read(connect_path)
    list_keys = {'database': config.get('db_connection', 'database'),
                 'port': config.get('db_connection', 'port'),
                 'host': config.get('db_connection', 'host'),
                 'sslmode': config.get('db_connection', 'sslmode'),
                 'user': config.get('db_connection', 'user'),
                 'password': config.get('db_connection', 'password')}
    return list_keys


def index(config_path):
    """
    Build a dictionary, given a configuration files
    :param config_path: Configuration path which contains a list of files that will be cleaned
    :return: Index object
    """
    with open(config_path) as config_file:
        data = yaml.load(config_file)
    if data is not None:
        index_words = defaultdict(lambda: defaultdict(list))
        for file_dirty in data['files_path']:
            opener = urllib.urlopen(file_dirty.get('file'))
            with contextlib.closing(opener) as source_file:
                read_source_file = source_file.readlines()
                # Used 1-based indexing for showing line numbers in output representation
                for i, line in enumerate(read_source_file, 1):
                    cleaned_line = clean_file.sanitize(line)
                    for word in cleaned_line.split():
                        index_words[word.lower()][source_file.url].append(i)
    else:
        raise ValueError('Empty configuration file')
    return index_words


def build_index(index_words, connect_path):
    """
    Insert the index in a specific database for store all data
    :param index_words: Object which contains the built index
    """
    db_keys = load_config_file(connect_path)
    connection = psycopg2.connect(database=db_keys.get('database'), user=db_keys.get('user'),
                                  password=db_keys.get('password'), host=db_keys.get('host'),
                                  port=db_keys.get('port'), sslmode=db_keys.get('sslmode'))
    count = 0
    try:
        with connection:
            with connection.cursor() as cursor:
                for word in index_words:
                    for file_path in index_words[word]:
                        data_select = (word, file_path)
                        cursor.execute(query_select, data_select)
                        if cursor.fetchall():
                            data_update = (index_words[word].get(file_path), word, file_path)
                            cursor.execute(query_update, data_update)
                        else:
                            data_insert = (word, file_path, index_words[word].get(file_path))
                            cursor.execute(query_insert, data_insert)
                        count += 1
                        print count
    finally:
        connection.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path')
    parser.add_argument('connect_path')
    args = parser.parse_args()
    try:
        index = index(args.config_path)
        build_index(index, args.connect_path)
    except IOError as e:
        print 'File or path not found: %s' % e
