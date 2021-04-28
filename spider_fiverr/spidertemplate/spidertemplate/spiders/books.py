import scrapy


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
            