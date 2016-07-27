import psycopg2
from load_config import load_config_file


class SearchEngine(object):
    def __init__(self, connect_path):
        self.connect_path = connect_path
        keys = load_config_file(self.connect_path)
        self.database = keys['database']
        self.user = keys['user']
        self.password = keys['password']
        self.port = keys['port']
        self.host = keys['host']
        self.sslmode = keys['sslmode']

    def search(self, search_word):
        """
        Search if a given word is in bucket of files
        :param search_word: Word given to search
        :return: List of tuples composed by the given word, file and all the occurrences found
        """
        result_search = []

        connection = psycopg2.connect(host=self.host, port=self.port, sslmode=self.sslmode,
                                      database=self.database, user=self.user, password=self.password)
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM index WHERE word = '%s';" % search_word)
                    result_search = cursor.fetchall()
        finally:
            connection.close()
        return result_search
