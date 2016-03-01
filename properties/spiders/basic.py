# -*- coding: utf-8 -*-
import scrapy
import re
from properties.items import PropertiesItem

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = (
        'http://web:9312/properties/property_000000.html/',
    )

    def parse(self, response):
	"""
        self.log("title:%s" %response.xpath('//*[@itemprop="name"][1]/text()').extract())
        self.log("price:%s" %response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+'))
        self.log("description:%s" %response.xpath('//*[@itemprop="description"][1]/text()').extract())
        self.log("address:%s" %response.xpath('//*[@itemtype="http://schema.org/Place"][1]/text()').extract())   
        self.log("image_urls:%s" %response.xpath('//*[@itemprop="image"][1]/@src').extract())     
	"""
	"""
	item=PropertiesItem()
	item['title']=response.xpath('//*[@itemprop="name"][1]/text()').extract()
	item['price']=response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
	item['description']=response.xpath('//*[@itemprop="description"][1]/text()').extract()
	item['address']=response.xpath('//*[@itemtype="http://schema.org/Place"][1]/text()').extract()
	item['image_urls']=response.xpath('//*[@itemprop="image"][1]/@src').extract()
	"""
	l=ItemLoader(item=PropertiesItem(),response=response)
	l.add_xpath('title','//*[@itemprop="name"][1]/text()')
	l.add_xpath('price','//*[@itemprop="price"][1]/text()',re='[.0-9]+')
	l.add_xpath('description','//*[@itemprop="description"][1]/text()')
	l.add_xpath('address','//*[@itemtype="http://schema.org/Place"][1]/text()')
	l.add_xpath('image_urls','//*[@itemprop="image"][1]/@src')

	return l.load_item()
	#return item
