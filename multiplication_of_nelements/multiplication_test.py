import unittest

from multiplication_of_nelements import multiplication_of_n_elements

class MultiplicationsOfNElementsTest(unittest.TestCase):

    def test_multiplication(self):
        array = [2, 3, 1, 4]
        array2 = [2, 2, 2, 2]
        array2 = array2 * 2
        print array2