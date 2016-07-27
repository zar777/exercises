from collections import defaultdict, Counter
from index import load_config_file
import psycopg2

QUERY_SELECT = "select * from index where word in %s;"


class SearchEngine(object):
    def __init__(self, connect_path):
        self.connect_path = connect_path

    def build_result_object(self, result, count_words, search_word):
        """
        In the method it's rebuilt the old data structure used to the differents kind of searching.
        It's used only if when it's looking for multiple words
        :param result:
        :param count_words:
        :param search_word:
        :return:
        """
        #
        result_search = []
        for key in result:
            if len(result.get(key)[0]) == count_words:
                counter = Counter(result.get(key)[1])
                line_numbers = []
                for line in counter:
                    if counter.get(line) == count_words:
                        line_numbers.append(line)
                if len(line_numbers) > 0:
                    result_search.append((search_word, key, line_numbers))
        return result_search

    def temp_object_multi_words(self, result_search, count_words):
        """
        In the section below the data structure is a dictionary in which the key is the FILE NAME and the values
        is a list made up: 1) a words list 2) an occurrences list of the given words
        :param result_search:
        :param count_words:
        :return: 
        """
        i = 0
        j = 1
        result = defaultdict(lambda: list)
        while i <= len(result_search) - 1:
            while j <= len(result_search) - 1:
                if result_search[i][1] == result_search[j][1]:
                    if result_search[i][1] in result:
                        if len(result.get(result_search[i][1])[0]) < count_words:
                            result.get(result_search[i][1])[0].append(result_search[j][0])
                            result.get(result_search[i][1])[1] += list(set(result_search[j][2]))
                        j += 1
                    else:
                        result[result_search[i][1]] = [[result_search[i][0], result_search[j][0]],
                                                       list(set(result_search[i][2])) + list(set(result_search[j][2]))]
                        j += 1
                else:
                    j += 1
            i += 1
            j = i + 1
        return result

    def search(self, search_word):
        """
        Search if a given word is in bucket of files
        :param search_word: Word given to search
        :return: List of tuples composed by the given word, file and all the occurrences found
        """
        result_search = []
        database = load_config_file(self.connect_path).get('database')
        user = load_config_file(self.connect_path).get('user')
        password = load_config_file(self.connect_path).get('password')
        port = load_config_file(self.connect_path).get('port')
        host = load_config_file(self.connect_path).get('host')
        sslmode = load_config_file(self.connect_path).get('sslmode')
        connection = psycopg2.connect(host=host, port=port, sslmode=sslmode,
                                      database=database, user=user, password=password)
        words = tuple(search_word.split(" "))
        count_words = len(words)
        if len(words) == 1:
            words += ("",)
            count_words = 1

        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(QUERY_SELECT, words)
                    result_search = cursor.fetchall()
            if count_words > 1:
                temp_result = self.temp_object_multi_words(result_search, count_words)
                result_search = self.build_result_object(temp_result, count_words, search_word)
        finally:
            connection.close()
        return result_search
