class DeleteDuplicates(object):
    def __init__(self, string):
        self.string = string

    def remove_duplicates(self):
        string_sorted = ''.join(sorted(self.string))
        new_string = ""
        last_character = ""
        for c in string_sorted:
            if c != last_character:
                last_character = c
                new_string += last_character
        return new_string

if __name__ == '__main__':
    string_one = "cacca"
    string_two = "ciao"
    string_three = "llla"
    string_four = "aaal"
    string_five = "aaalcccc"
    delete_class = DeleteDuplicates(string_one)
    print delete_class.remove_duplicates()
    print string_one
    delete_class = DeleteDuplicates(string_two)
    print delete_class.remove_duplicates()
    delete_class = DeleteDuplicates(string_three)
    print delete_class.remove_duplicates()
    delete_class = DeleteDuplicates(string_four)
    print delete_class.remove_duplicates()
    delete_class = DeleteDuplicates(string_five)
    print delete_class.remove_duplicates()