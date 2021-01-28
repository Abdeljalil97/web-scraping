import scrapy
import socket
import datetime
from scrapy.loader.processors import MapCompose, Join
from ..items import ProporotiesItem
from scrapy.loader import ItemLoader
class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['gumtree.com']
    start_urls = ['https://www.gumtree.com/p/commercial-property-to-rent/commercial-office-studio-workshop-space-rent-your-space-today/1385881841']

    def parse(self, response):
        """ This function parses a property page.
         @url http://web:9312/properties/property_000000.html
         @returns items 1
         @scrapes title price description address image_urls
         @scrapes url project spider server date
         """
        l = ItemLoader(item=ProporotiesItem(), response=response)
        l.add_xpath('title','//*[@id="ad-title"]/text()',MapCompose(str.strip, str.title))
        l.add_xpath('price','//*[@class="ad-price txt-xlarge txt-emphasis inline-block"]/text()',MapCompose(lambda i: i.replace(',', ''), float),re='[.0-9]+')
        l.add_xpath('description','//*[@itemprop="description"][1]/text()', MapCompose(str.strip), Join())
        l.add_xpath('address','//*[@itemtype="http://schema.org/Place"]/span[@itemprop="address"]/text()',MapCompose(str.strip))
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()
