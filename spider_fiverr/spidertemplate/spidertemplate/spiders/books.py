import scrapy
#Imports below used to test fake response
import os
from scrapy.http import Request, TextResponse

def fake_response(file_name=None, url=None):
    """Create a Scrapy fake HTTP response from a HTML file"""
    if not url:
        url = 'https://books.toscrape.com/'

    request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name

        file_content = open(file_path, 'r').read()
    else:
        file_content = ''

    response = TextResponse(url=url, request=request, body=file_content, encoding='utf-8')
    
    return response


class BooksSpider(scrapy.Spider):
    name = 'book'
    start_urls = ['https://books.toscrape.com/']
    
    ##Use scrapys built in parse function to scrape the urls
    def parse(self, response):
        for products in response.css('article.product_pod'):
        ##Create a try and except to avoid errors when parsing ou tof stock products
            try:
                yield {
                    'price': products.css('p.price_color::text').get().replace('£', ''),
                    'link': products.css('a').attrib['href'],
                }
            except:
                yield {
                    'price': 'Sold Out',
                    'link': products.css('a').attrib['href'],
                }
        ##
        next_page = response.css('li.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            