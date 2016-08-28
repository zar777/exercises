import re


class MicrosoftParser(object):

    def __init__(self, text, file_surname, file_women, file_men):
        self.text = text
        self.file_surname = file_surname
        self.file_women = file_women
        self.file_men = file_men

    def sanitize(self, line):
        """
        Support the clean up operation deleting all the punctuation except characters: - ' @ .
        :param line: string to clean
        :return: new line cleaned
        """
        # This regex deletes all the punctuation and the strings of length 1, in order to simplify
        # the search and find the right result.
        return re.sub(ur"([^\w\d\s]+|_)", '', line)

    def parser(self):
        word_offset = self.save_data()
        name_surname = self.construct_db()
        match = {}
        i = 0
        j = i+1
        while j < len(word_offset):
            if word_offset[i][0] in name_surname[0] and word_offset[j][0] in name_surname[1]:
                key_name_surname = str('%s %s' % (word_offset[i][0], word_offset[j][0]))
                if key_name_surname in match:
                    match[key_name_surname].append(word_offset[i][1])
                else:
                    match[key_name_surname] = [word_offset[i][1]]
            i += 1
            j = i+1
        return match

    def save_data(self):
        word_offset = []
        offset = 1
        clean_string = self.sanitize(self.text)
        for word in clean_string.split(" "):
            word_offset.append((word, offset))
            offset += len(word)+1
        return word_offset

    def construct_db(self):
        surname_set = set()
        name_set = set()
        with open(self.file_surname) as file_sur:
            for line in file_sur:
                surname_set.add(line.lower().strip().rstrip("/n"))
        tmp = [self.file_women, self.file_men]
        for fil in tmp:
            with open(fil) as f:
                for line in f:
                    name_set.add(line.lower().strip().rstrip("/n"))
        return name_set, surname_set




