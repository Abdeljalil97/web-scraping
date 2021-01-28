import scrapy

queries = ['tshirt for man', "tshirt for women"]
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?']

    def parse(self, response):
        def start_requests(self):
            for query in queries:
                url = 'https://www.amazon.com/s?' + urlencode({'k': query})
                yield scrapy.Request(url=url, callback=self.parse_keyword_response)
