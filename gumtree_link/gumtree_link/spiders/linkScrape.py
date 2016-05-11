# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
import pymongo
import lxml.html

class LinkscrapeSpider(scrapy.Spider):
    name = "linkScrape"
    allowed_domains = []
    start_urls = (
        'http://www.gumtree.com.au/s-canberra/l3002977r50?fromSearchBox=true',
    )

    def __init__(self):
	self.init_mongo()
    
    def init_mongo(self):
	self.client = pymongo.MongoClient('localhost',27017)
	self.db = self.client.gumtree
	
    def collect_info(self,selector):
	title = selector.cssselect('h6[class=rs-ad-title]')[0].text_content().strip('\n\r\t').strip()
	price = selector.cssselect('span[class=j-original-price]')[0].text_content().strip('\n\r\t').strip()
	location = selector.cssselect('div[class="rs-ad-field rs-ad-location"]')[0].text_content().strip('\n\r\t').replace('  ','')
	description = selector.cssselect('p[class="rs-ad-description c-word-wrap"]')[0].text_content().strip('\n\r\t').strip()
	date = selector.cssselect('div[class=rs-ad-date]')[0].text_content().strip('\n\r\t').strip()
	link = selector.cssselect('a[itemprop=url]')[0].get('href')
	link = 'http://www.gumtree.com.au/'+link
	name = ''
	mobile = ''
	fetch = 0
	myid = self.db.gumtree_link.count()
	item = dict(Title=title,Price=price,Location=location,Name=name,Mobile=mobile,Description=description,TimeStamp=date,Link=link,Fetch=fetch,Id=myid)
	self.db.gumtree_link.insert(item)


    def parse(self,response):
	tree = lxml.html.fromstring(response.body)
	selectors = tree.cssselect('div[class=rs-ad-information]')
	for selector in selectors:
	    self.collect_info(selector)
	
	next_page = response.xpath('//a[@class="rs-paginator-btn next"]/@href').extract()
	next_page = next_page[0]
	next_link = urlparse.urljoin('http://www.gumtree.com.au/',next_page)
	print '--------------------------------------------'
	print next_link
	print '---------------------------------------------'
	yield Request(next_link,callback=self.parse)
	

