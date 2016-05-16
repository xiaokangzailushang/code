# -*- coding: utf-8 -*-
import scrapy
import re
import urllib2

class PandoraSpiderSpider(scrapy.Spider):
    name = "pandora_spider"
    allowed_domains = []
    start_urls = (
    )

    def __init__(self):
	fb = open('/home/jun/git/code/pandora/bracelets_link.txt','rb')
	lines = fb.readlines()
	for line in lines:
	    self.start_urls = self.start_urls + (line,)

    def parse_url(self,url):
	info = {}
	tmp = url.split('/')
	info['category']=tmp[3]
	if info['category']== 'necklaces':
		info['category']='necklaces-and-pendants'
	tmp = tmp[-1]
	pattern = re.compile(r'[^/]+\.html')
	result = pattern.search(url)
	filename = ''
	if result:
		filename = result.group()[0:-5]
	info['name']=filename	
	return info

    def save_jpg(self,url,filename):
	res = urllib2.urlopen(url)
	tmp = open(filename,'wb')
	tmp.write(res.read())
	tmp.close()

    def parse(self, response):
        try:
	    jpg_url = response.xpath('//a[@class="product-image main-image"]/@href').extract()
	    jpg_url = jpg_url[0]
	except Exception,e:
	    jpg_url = ''
	try:
	    price = response.xpath('//fieldset//span[@class="price-sales "]/text()').extract()
	    price = price[0]
	    
	except Exception,e:
	    price = "$0"
	info = self.parse_url(response.url)
	if jpg_url != '':
	    self.save_jpg(url=jpg_url,filename=info['name']+'_'+price)
	
	
