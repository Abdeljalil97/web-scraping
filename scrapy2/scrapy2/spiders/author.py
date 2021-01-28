import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.xpath('//*[@class="author"]/a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.xpath('//*[contains(@class,"next")]/a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get(default='').strip()

        yield {
            'name': extract_with_xpath('//*[@class="author-title"]/text()'),
            'birthdate': extract_with_xpath('//*[@class="author-born-date"]/text()'),
            'bio': extract_with_xpath('//*[@class="author-description"]/text()'),
        }
