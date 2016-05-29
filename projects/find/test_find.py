import os
import unittest
from find import find
from mock import patch
from cStringIO import StringIO


def mock_islink(arg):
    if arg in {'test.link', 'tree.link'}:
        return True
    return False


def mock_isdir(arg):
    _, filename = os.path.split(arg)
    if filename in {'test', 'test_subdir', 'test_folder'}:
        return True
    return False


class FindTest(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_mock_find(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'], ['subtest_dir'], ['cc', 'dd']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        find('/home/user/test_folder', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n/home/user/test_folder/f.csv\n'
                      '/home/user/test_folder/test\n/home/user/test_folder/zz.xls\n'
                      '/home/user/test_folder/test/subtest_dir\n')
        self.assertEqual(golden_out, self.out.getvalue())

    def test_link_find(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'test.link']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        find('/home/user/test_folder', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n/home/user/test_folder/f.csv\n'
                      '/home/user/test_folder/test\n/home/user/test_folder/zz.xls\n'
                      '/home/user/test_folder/test/subtest_dir\n')
        self.assertEqual(golden_out, self.out.getvalue())

    def test_empty_folder(self):
        with patch('os.listdir', side_effect=[[]]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        find('/home/user/test_folder', out=self.out)
        golden_out = '/home/user/test_folder\n'
        self.assertEqual(golden_out, self.out.getvalue())

    def test_folder_not_exist(self):
        with patch('os.path.exists', return_value=False):
            self.assertRaises(ValueError, find, '/home/user/test_folder')
if __name__ == '__main__':
    unittest.main()
