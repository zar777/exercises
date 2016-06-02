import unicodedata
import sys

table = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))


def remove_punctuations(line):
    a = line.decode('utf-8').translate(table)
    return a


def clean_up(src_path, dest_path):
    with open(src_path) as source_file:
        with open(dest_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(remove_punctuations(line).encode('utf-8'))


if __name__ == '__main__':
    clean_up('/home/gianluca/Desktop/news', '/home/gianluca/Desktop/write_file')