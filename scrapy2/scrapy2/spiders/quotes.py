import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            content = quote.xpath('.//*[@itemprop="text"]/text()').extract_first()
            author  =  quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags    =    quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            yield {'quote':content, 'author':author, 'tags':tags}


        pagination_links = response.xpath('//*[contains(@class,"next")]/a')
        yield from response.follow_all(pagination_links, self.parse)

