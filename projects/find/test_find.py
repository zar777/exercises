import os
import unittest
from find import find
from mock import patch
from cStringIO import StringIO


def mock_islink(arg):
    _, filename = os.path.split(arg)
    if filename in {'test.link', 'tree.link'}:
        return True
    return False


def mock_isdir(arg):
    _, filename = os.path.split(arg)
    if filename in {'test', 'subtest_dir', 'test_older', 'test_folder', 'aaa', 'telephone'}:
        return True
    return False


class FindTest(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def test_find(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'], ['subtest_dir'], ['cc', 'dd']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.exists', return_value=True):
                    find('/home/user/test_folder', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n/home/user/test_folder/f.csv\n'
                      '/home/user/test_folder/test\n/home/user/test_folder/test/subtest_dir\n'
                      '/home/user/test_folder/test/subtest_dir/cc\n/home/user/test_folder/test/subtest_dir/dd\n'
                      '/home/user/test_folder/zz.xls\n'
)
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__link(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'test.link']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        with patch('os.path.realpath', return_value='/doc/file.txt'):
                            find('/home/user/test_folder', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n/home/user/test_folder/f.csv\n'
                      '/home/user/test_folder/test\n/home/user/test_folder/test/subtest_dir\n'
                      '/home/user/test_folder/test/subtest_dir/cc\n/home/user/test_folder/test/subtest_dir/dd\n'
                      '/home/user/test_folder/test/subtest_dir/test.link->/doc/file.txt\n'
                      '/home/user/test_folder/zz.xls\n'
)
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__cycle_link(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'test.link']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        with patch('os.path.realpath', return_value='/home/user/test_folder'):
                            find('/home/user/test_folder', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n/home/user/test_folder/f.csv\n'
                      '/home/user/test_folder/test\n/home/user/test_folder/test/subtest_dir\n'
                      '/home/user/test_folder/test/subtest_dir/cc\n/home/user/test_folder/test/subtest_dir/dd\n'
                      '/home/user/test_folder/test/subtest_dir/test.link->/home/user/test_folder\n'
                      '/home/user/test_folder/zz.xls\n'
                      )
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__empty_folder(self):
        with patch('os.listdir', side_effect=[[]]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.exists', return_value=True):
                    find('/home/user/test_folder', out=self.out)
        golden_out = '/home/user/test_folder\n'
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__folder_not_exist(self):
        with patch('os.path.exists', return_value=False):
            self.assertRaises(ValueError, find, '/home/user/test_folder')

    # Tests for -name function
    def test_find__name(self):
        with patch('os.listdir', side_effect=[['z.csv', 'test', 'azz.txt', 'zz.xls'], ['subtest_dir'], ['token', 'zz']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.exists', return_value=True):
                    find('/home/user/test_folder', 'zz', out=self.out)
        golden_out = ('/home/user/test_folder/azz.txt\n/home/user/test_folder/test/subtest_dir/zz\n'
                      '/home/user/test_folder/zz.xls\n')

        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__name_link(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'tree.link']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        with patch('os.path.realpath', return_value='/doc/file.txt'):
                            find('/home/user/test_older', 'tree', out=self.out)
        golden_out = '/home/user/test_older/test/subtest_dir/tree.link->/doc/file.txt\n'
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__cycle_name_link(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'test.link']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        with patch('os.path.realpath', return_value='/home/user/test_folder'):
                            find('/home/user/test_folder', 'test.link', out=self.out)
        golden_out = '/home/user/test_folder/test/subtest_dir/test.link->/home/user/test_folder\n'
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__name_empty_folder(self):
        with patch('os.listdir', side_effect=[[]]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.exists', return_value=True):
                    find('/home/user/test_folder', 'fol', out=self.out)
        golden_out = '/home/user/test_folder\n'
        self.assertEqual(golden_out, self.out.getvalue())

    def test_find__folder_name_link(self):
        with patch('os.listdir', side_effect=[['f.csv', 'test', 'a.txt', 'zz.xls'],
                                              ['subtest_dir'], ['cc', 'dd', 'test.link'],
                                              ['try.txt', 'text.txt', 'telephone'], ['trichard.txt']]):
            with patch('os.path.isdir', side_effect=mock_isdir):
                with patch('os.path.islink', side_effect=mock_islink):
                    with patch('os.path.exists', return_value=True):
                        with patch('os.path.realpath', return_value='/aaa'):
                            find('/home/user/test_folder', 'a', out=self.out)
        golden_out = ('/home/user/test_folder\n/home/user/test_folder/a.txt\n'
                      '/home/user/test_folder/f.csv\n/home/user/test_folder/test\n'
                      '/home/user/test_folder/test/subtest_dir\n/home/user/test_folder/test/subtest_dir/cc\n'
                      '/home/user/test_folder/test/subtest_dir/dd\n'
                      '/home/user/test_folder/test/subtest_dir/test.link->/try\n/try/telephone\n'
                      '/try/telephone/trichard.txt\n/try/text.txt\n/try/try.txt\n/home/user/test_folder/zz.xls\n')
        self.assertEqual('', self.out.getvalue())

if __name__ == '__main__':
    unittest.main()
