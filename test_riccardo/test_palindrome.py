import unittest
import palindome


class PalindomeTest(unittest.TestCase):

    s = None
    s1 = None
    s2 = None
    s3 = None
    s4 = None
    s5 = None
    s6 = None
    s7 = None

    def setUp(self):
        self.s = "Go hang a salami I'm a lasagna hog."
        self.s1 = "Was it a rat I saw?"
        self.s2 = "Sit on a potato pan, Otis"
        self.s3 = "Lisa Bonet ate no basi"
        self.s4 = "Satan, oscillate my metallic sonatas"
        self.s5 = "I roamed under it as a tired nude Maori"
        self.s6 = "Rise to vote sir"
        self.s7 = "Dammit, I'm mad!"

    def test_sanitize_s(self):
        self.assertEqual(palindome.sanitize(self.s), 'gohangasalamiimalasagnahog')

    def test_sanitize_s1(self):
        self.assertEqual(palindome.sanitize(self.s1), 'dammitimmad')

    def test_sanitize_s2(self):
        self.assertEqual(palindome.sanitize(self.s2), 'wasitaratisaw')

    def test_sanitize_s3(self):
        self.assertEqual(palindome.sanitize(self.s3), 'sitonapotatopanotis')

    def test_sanitize_s4(self):
        self.assertEqual(palindome.sanitize(self.s4), 'lisabonetatenobasi')

    def test_sanitize_s5(self):
        self.assertEqual(palindome.sanitize(self.s5), 'satanoscillatemymetallicsonatas')

    def test_sanitize_s6(self):
        self.assertEqual(palindome.sanitize(self.s6), 'risetovotesir')

    def test_sanitize_s7(self):
        self.assertEqual(palindome.sanitize(self.s7), 'dammitimmad')

    def test_is_palindome_false(self):
        self.assertFalse(palindome.is_palindrome("ciao"))

    def test_is_palindome_empty_string(self):
        self.assertTrue(palindome.is_palindrome(""))

    def test_is_palindome_punctuation(self):
        self.assertTrue(palindome.is_palindrome("!!!!!"))

    def test_is_palindome_s(self):
        self.assertTrue(palindome.is_palindrome(self.s))

    def test_is_palindome_s1(self):
        self.assertTrue(palindome.is_palindrome(self.s1))

    def test_is_palindome_s2(self):
        self.assertTrue(palindome.is_palindrome(self.s2))

    def test_is_palindome_s3(self):
        self.assertTrue(palindome.is_palindrome(self.s3))

    def test_is_palindome_s4(self):
        self.assertTrue(palindome.is_palindrome(self.s4))

    def test_is_palindome_s5(self):
        self.assertTrue(palindome.is_palindrome(self.s5))

    def test_is_palindome_s6(self):
        self.assertTrue(palindome.is_palindrome(self.s6))

    def test_is_palindome_s7(self):
        self.assertTrue(palindome.is_palindrome(self.s7))