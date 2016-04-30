class UniqueCharacters(object):
    """this class represents an empty dictionary dictionary"""
    def __init__(self):
        self.dictionary = {}

    def unique(self, string):
        """this method is created to return the first child, given his parent"""
        count = 0
        numbers_occurrence = 0
        if string != "":
            for letter in string:
                if letter not in self.dictionary:
                    self.dictionary[letter] = 0
                else:
                    count += 1
                    self.dictionary[letter] = 1

        return count

if __name__ == '__main__':
    string = "parallelo"
    unique_characters = UniqueCharacters()
    print string
    print unique_characters.unique(string)
    print unique_characters.dictionary


