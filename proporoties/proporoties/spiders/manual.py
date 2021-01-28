import scrapy


class ManualSpider(scrapy.Spider):
    name = 'manual'
    start_urls = ['https://gumtree.com/flats-houses/london/']

    def parse(self, response):
        pass
