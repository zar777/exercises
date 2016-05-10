import unittest

from delete_duplicates import DeleteDuplicates


class DeleteDuplicatesTest(unittest.TestCase):

    def test_all_cases(self):
        string_one = "cacca"
        string_two = "ciao"
        string_three = "llla"
        string_four = "aaal"
        string_five = "aaalcccc"
        delete_class = DeleteDuplicates(string_one)
        self.assertNotEqual(delete_class.remove_duplicates(), string_one)
        delete_class = DeleteDuplicates(string_two)
        self.assertNotEqual(delete_class.remove_duplicates(), string_two)
        delete_class = DeleteDuplicates(string_three)
        self.assertNotEqual(delete_class.remove_duplicates(), string_three)
        delete_class = DeleteDuplicates(string_four)
        self.assertNotEqual(delete_class.remove_duplicates(), string_four)
        delete_class = DeleteDuplicates(string_five)
        self.assertNotEqual(delete_class.remove_duplicates(), string_five)