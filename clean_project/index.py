"""
Create a JSON file used to indexing all words in a config_file.yaml
"""
import argparse
import codecs
import psycopg2
import yaml

from collections import defaultdict
import clean_file


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
            with codecs.open(file_dirty.get('file'), 'r', 'utf-8') as source_file:
                # Used 1-based indexing for showing line numbers in output representation
                for i, line in enumerate(source_file, 1):
                    cleaned_line = clean_file.sanitize(line)
                    for word in cleaned_line.split():
                        index_words[word.lower()][source_file.name].append(i)
    else:
        raise ValueError('Empty configuration file')
    return index_words


def build_index(index_words):
    """
    Insert the index in a specific database for store all data
    :param index_words: Object which contains the built index
    """
    connection = None
    try:
        connection = psycopg2.connect(database='index_db', user='gianluca', password='password')
        cursor = connection.cursor()
        query_update = "UPDATE index SET occurrences=%s WHERE word=%s AND file=%s;"

        query_insert = ("INSERT INTO index (word, file, occurrences)"
                        "SELECT %s, %s, %s"
                        "WHERE NOT EXISTS (SELECT 1 FROM index WHERE word=%s AND file=%s);")
        for word in index_words:
            for file_path in index_words[word]:
                data_update = (index_words[word].get(file_path), word, file_path)
                cursor.execute(query_update, data_update)
                data_insert = (word, file_path, index_words[word].get(file_path), word, file_path)
                cursor.execute(query_insert, data_insert)
                connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()
        print 'Error %s' % e

    finally:

        if connection:
            connection.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path')
    args = parser.parse_args()
    try:
        index = index(args.config_path)
        build_index(index)
    except IOError as e:
        print 'File or path not found: %s' % e
