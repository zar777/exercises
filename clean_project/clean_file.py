import argparse
import codecs
import re


def clean_up(src_path, dest_path):
    """
    This method is created to open a file, clean up and write it in another new file
    :param src_path: source path
    :param dest_path: destination path of new file
    """
    with codecs.open(src_path, "r", "utf-8") as source_file:
        with codecs.open(dest_path, "w", "utf-8") as dest_file:
            for line in source_file:
                new_line = sanitize(line)
                dest_file.write(new_line)


def sanitize(line):
    """
    this method is created to support the clean up operation deleting all the punctuation except characters: - ' _ @ .
    :param line: string to clean
    :return: new line cleaned
    """
    return re.sub(ur"[^.\w@\d'\s-]+", '', line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    try:
        clean_up(args.input, args.output)
    except IOError as e:
        print "File or path not found: %s" % e