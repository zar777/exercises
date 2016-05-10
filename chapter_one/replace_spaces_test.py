import unittest

from replace_spaces import  ReplaceSpaces

class ReplaceSpacesTest(unittest.TestCase):

    def test_replace_with_array(self):
        string = "ciao come stai ?"
        string_two = "    "
        string_three = "ciaocomestai?"
        replace_space = ReplaceSpaces(string)
        self.assertNotEqual(replace_space.replace_with_array(), string)
        self.assertEqual(replace_space.replace_with_array(), "ciao%20come%20stai%20?")
        replace_space = ReplaceSpaces(string_two)
        self.assertNotEqual(replace_space.replace_with_array(), string_two)
        self.assertEqual(replace_space.replace_with_array(), "%20%20%20%20")
        replace_space = ReplaceSpaces(string_three)
        self.assertEqual(replace_space.replace_with_array(), string_three)


    def test_replace_with_string(self):
        string = "ciao come stai ?"
        string_two = "    "
        string_three = "ciaocomestai?"
        replace_space = ReplaceSpaces(string)
        self.assertNotEqual(replace_space.replace_with_string(), string)
        self.assertEqual(replace_space.replace_with_string(), "ciao%20come%20stai%20?")
        replace_space = ReplaceSpaces(string_two)
        self.assertNotEqual(replace_space.replace_with_string(), string_two)
        self.assertEqual(replace_space.replace_with_string(), "%20%20%20%20")
        replace_space = ReplaceSpaces(string_three)
        self.assertEqual(replace_space.replace_with_string(), string_three)
