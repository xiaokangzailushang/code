# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem


class LoginSpider(CrawlSpider):
    name = 'login'
    allowed_domains = ['web']
    #start_urls = ['http://web:9312/dynamic/login']
    #start with a login request
    def start_requests(self):
        return [ FormRequest("http://web:9312/dynamic/login",formdata={"user":"user","pass":"pass"})]


    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@class="next"]')),
	Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'),callback='parse_item')
    )

    def parse_item(self, response):
        
	l=ItemLoader(item=PropertiesItem(),response=response)
	l.add_xpath('title','//*[@itemprop="name"][1]/text()')
	l.add_xpath('price','//*[@itemprop="price"][1]/text()',re='[.0-9]+')
	l.add_xpath('description','//*[@itemprop="description"][1]/text()')
	l.add_xpath('address','//*[@itemtype="http://schema.org/Place"][1]/text()')
	l.add_xpath('image_urls','//*[@itemprop="image"][1]/@src')

	return l.load_item()
	#return item
