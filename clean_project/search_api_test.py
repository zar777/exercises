import json
import search_api
import search_engine
import unittest

from index_test import convert


class SearchApiTest(unittest.TestCase):
    def setUp(self):
        self.search_obj = search_engine.SearchEngine('test_data/config.cfg')
        self.tester = search_api.config_app(self.search_obj).test_client(self)

    def test_match(self):
        response = self.tester.get('/search/bush', content_type='application/json')
        convert_result = convert(json.loads(response.data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(convert_result, {u'search_response':
                                                         {u'bush': {u'test_data/full_file_dirty.txt': [1]}}})

    def test_no_word(self):
        response = self.tester.get('/search/', content_type='text/html')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(str(response), '<Response streamed [404 NOT FOUND]>')

    def test_no_match(self):
        response = self.tester.get('/search/fakeword', content_type='application/json')
        convert_result = convert(json.loads(response.data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(convert_result, {u'search_response': {}})

if __name__ == '__main__':
    unittest.main()
