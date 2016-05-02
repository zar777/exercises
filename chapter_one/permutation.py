class Permutation(object):
    """Exercises 1.3 : given two strings, write a method to decide if one is a permutation of the other"""
    def __init__(self):
        self.alphabet = [0] * 26

    def detect_permutation(self, string_one, string_two):
        """this method is created verify if, given two strings, one is a permutation of the other"""
        count = 0
        for letter_one in string_one:
            position = ord(letter_one) - ord("a")
            self.alphabet[position] += 1

        for letter_two in string_two:
            position = ord(letter_two) - ord("a")
            self.alphabet[position] -= 1

        while count < self.alphabet.__len__():
            if self.alphabet[count] != 0:
                return False
            else:
                count += 1
        return True

if __name__ == '__main__':
    string_one = "ciao"
    string_two = "oaic"
    permutation = Permutation()
    print permutation.alphabet.__len__()
    print permutation.alphabet
    print string_one
    print string_two
    print ord('c')
    print ord('a')
    print ord('c')-ord('a')
    print Permutation().detect_permutation(string_one, string_two)


