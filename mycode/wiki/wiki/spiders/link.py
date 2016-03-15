# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
from scrapy.loader import ItemLoader
from wiki.items import WikiItem

pages =  set()
class LinkSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Kevin_Bacon',
    )

    def parse(self, response):
        global pages
        item = WikiItem()
        next_links=response.xpath('//@href').extract()
        for link in next_links:
            link = urlparse.urljoin(response.url,link)
            if link not in pages:
                pages.add(link)
                item['link']=link
		item['parent']=response.url
                yield Request(link)

        yield item


