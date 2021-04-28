from spidertemplate.spidertemplate.spiders.books import BooksSpider
import unittest
import books

class TestBooks(unittest.TestCase):
    
    def setUp(self):
        self.spider = BooksSpider()

    def test_parse(self):
        response = fake_response('input.html')
        item = self.spider.parse(response)
        self.assertEqual(item['title'], 'My Title')
        