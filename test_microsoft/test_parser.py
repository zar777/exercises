import unittest

from test_microsoft.microsoft_parser import MicrosoftParser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.text = "a small city 'gianluca' parente valeria a riccardo vitale2 gianmarco parente, gianluca parente!"
        self.surname = "files/surnames"
        self.men = "files/name_men"
        self.women = "files/name_women"
        self.parser = MicrosoftParser(self.text, self.surname, self.women, self.men)

    def test_save_data(self):
        self.assertEqual(self.parser.save_data(), [('a', 1), ('small', 3), ('city', 9), ('gianluca', 14),
                                                   ('parente', 23), ('valeria', 31), ('a', 39),
                                                   ('riccardo', 41), ('vitale2', 50), ('gianmarco', 58),
                                                   ('parente', 68), ('gianluca', 76), ('parente', 85)])

    def test_construct_db(self):
        self.assertEqual(self.parser.construct_db(), (set(['valeria', 'gianmarco', 'riccardo', 'giorgia', 'gianluca',
                                                           'giordano', 'lorenzo', 'martina', 'marta']),
                                                      set(['vitale', 'parente', 'lucherini', 'montella', 'cartesiani'])))

    def test_parser(self):
        self.assertEqual(self.parser.parser(), {'gianluca parente': [14, 76], 'gianmarco parente': [58]})

    def test_empty_text(self):
        self.parser.text = ""
        self.assertEqual(self.parser.save_data(), [('', 1)])
        self.assertEqual(self.parser.parser(), {})

    def test_empty_files(self):
        surname = "files/empty"
        men = "files/empty"
        women = "files/empty"
        parser = MicrosoftParser(self.text, surname, women, men)
        self.assertEqual(parser.construct_db(), (set([]), set([])))
        self.assertEqual(parser.parser(), {})