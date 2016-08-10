import unittest

from ellys_candy_bags import EllysCandyBags


class EllysCandyBagsTest(unittest.TestCase):

    def setUp(self):
        self.solution = EllysCandyBags()

    def test_zero(self):
        packets = ["FOO", "BAR", "BAZ", "TOPCODER"]
        self.assertEqual(5, self.solution.getSize(packets))

    def test_one(self):
        packets = ["X"]
        self.assertEqual(0, self.solution.getSize(packets))

    def test_two(self):
        packets = ["GIVING", "CANDY", "TO", "CHILDREN", "CANNOT", "BE", "CHALLENGING", "RIGHT"]
        self.assertEqual(17, self.solution.getSize(packets))

    def test_three(self):
        packets = ["WITHOUT", "IT", "IM", "JUST", "ESPR"]
        self.assertEqual(5, self.solution.getSize(packets))

    def test_four(self):
        packets = ["PHQGHUMEAYLNLFDXFIRCVSCXGGBWKFNQDUXWFNFOZVSRTKJPRE",
                 "PGGXRPNRVYSTMWCYSYYCQPEVIKEFFMZNIMKKASVWSRENZKYCXF",
                 "XTLSGYPSFADPOOEFXZBCOEJUVPVABOYGPOEYLFPBNPLJVRVIPY",
                 "AMYEHWQNQRQPMXUJJLOOVAOWUXWHMSNCBXCOKSFZKVATXDKNLY",
                 "JYHFIXJSWNKKUFNUXXZRZBMNMGQOOKETLYHNKOAUGZQRCDDIUT",
                 "EIOJWAYYZPVSCMPSAJLFVGUBFAAOVLZYLNTRKDCPWSRTESJWHD",
                 "IZCOBZCNFWLQIJTVDWVXHRCBLDVGYLWGBUSBMBORXTLHCSMPXO",
                 "HGMGNKEUFDXOTOGBGXPEYANFETCUKEPZSHKLJUGGGEKJDQZJEN",
                 "PEVQGXIEPJSRDZJAZUJL"]
        self.assertEqual(203, self.solution.getSize(packets))