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


# connection to amazon instance : ssh -i ~/.ssh/AwsKey.pem ubuntu@50.112.85.84
# connection to amazon server : psql -h indexdb.c0awqz4pgr31.us-west-2.rds.amazonaws.com -d indexdb -p 5432 -U gianluca