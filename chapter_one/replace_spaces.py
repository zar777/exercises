"""Write a method to replace all spaces in a string with %20 Exercises 1.5"""
class ReplaceSpaces(object):
    def __init__(self, string):
        self.string = string

    def replace_with_array(self):
        array = self.string.split(" ")
        string_replaced = ""
        count = 0
        while count < len(array):
            if 0 <= count < len(array)-1:
                string_replaced += array[count]+"%20"
                count += 1
            else:
                string_replaced += array[count]
                count += 1
        return string_replaced

    def replace_with_string(self):
        string_replaced = ""
        for c in self.string:
            if c == " ":
                string_replaced += "%20"
            else:
                string_replaced += c
        return string_replaced



if __name__ == '__main__':
    string = "ciao come stai ?"
    string_two = "    "
    string_three = "ciaocomestai?"
    replace_space = ReplaceSpaces(string)
    print replace_space.replace_with_array()
    replace_space = ReplaceSpaces(string_two)
    print replace_space.replace_with_array()
    replace_space = ReplaceSpaces(string_three)
    print replace_space.replace_with_array()
    replace_space = ReplaceSpaces(string)
    print replace_space.replace_with_string()
    replace_space = ReplaceSpaces(string_two)
    print replace_space.replace_with_string()
    replace_space = ReplaceSpaces(string_three)
    print replace_space.replace_with_string()

