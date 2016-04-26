# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
import re

class LinkscrapeSpider(scrapy.Spider):
    name = "linkScrape"
    allowed_domains = []
    start_urls = (
        'http://www.gumtree.com.au/s-canberra/l3002977r50?fromSearchBox=true',
    )

    def parse(self,response):
	selectors = response.xpath('//h6[@class="rs-ad-title"]')
	self.parse_name_link(selectors)
	#links = response.xpath('//h6[@class="rs-ad-title"]/a/@href').extract()
	#for link in links:
	#    print(urlparse.urljoin('http://www.gumtree.com.au/',link))
	
	next_page = response.xpath('//a[@class="rs-paginator-btn next"]/@href').extract()
	next_page = next_page[0]
	next_link = urlparse.urljoin('http://www.gumtree.com.au/',next_page)
	print '--------------------------------------------'
	print next_link
	print '---------------------------------------------'
	yield Request(next_link,callback=self.parse)
	

    def parse_name_link(self,selectors):
	pattern_link = re.compile(r'\<a itemprop="url" .*href="(.+)".*')
	data = selectors.extract()
	#pattern_name = re.compile(
	for item in data:
	    print pattern_link.findall(item)
