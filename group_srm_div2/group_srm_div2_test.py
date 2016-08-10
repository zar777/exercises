import unittest

from group_srm_div2 import GroupSRMDiv2


class GroupSrmDiv2Test(unittest.TestCase):

    def setUp(self):
        self.solution = GroupSRMDiv2

    def test_zero(self):
        members = [1,1]
        self.assertEqual(2, self.solution().FindGroups(members))

    def test_one(self):
        members = [1,2]
        self.assertEqual(-1, self.solution().FindGroups(members))

    def test_two(self):
        members = [2, 2]
        self.assertEqual(1, self.solution().FindGroups(members))

    def test_three(self):
        members = [2, 2, 3, 3, 3]
        self.assertEqual(2, self.solution().FindGroups(members))

    def test_four(self):
        members = [3, 3, 2,2,2]
        self.assertEqual(-1, self.solution().FindGroups(members))

    def test_five(self):
        members = [2,3,2,3,2,3,2,1,1,2,2]
        self.assertEqual(6, self.solution().FindGroups(members))