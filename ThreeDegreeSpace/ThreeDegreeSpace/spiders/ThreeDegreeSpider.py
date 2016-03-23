# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
import re

class ThreedegreespiderSpider(scrapy.Spider):
    name = "ThreeDegreeSpider"
    allowed_domains = ["example.webscraping.com"]
    start_urls = (
        'http://example.webscraping.com',
    )
    Space_1st=[]
    Space_2nd=[]
    Space_3rd=[]
    pattern = re.compile(r"/+")

    def parse(self, response):
        links = response.xpath('//*[@href]/@href')
	for link in links.extract():
	    newUrl = urlparse.urljoin(response.url,link)		
	    if newUrl not in self.Space_1st:
	        self.Space_1st.append(newUrl)
		yield Request(newUrl,callback=self.parse_2nd_degree_space)
	

    def parse_2nd_degree_space(self,response):
	fn = self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
	    f.write(response.body)
	f.close()
	links = response.xpath('//*[@href]/@href')
	for link in links.extract():
	    newUrl = urlparse.urljoin(response.url,link)		
	    if newUrl not in self.Space_2nd and newUrl not in self.Space_1st:
	        self.Space_2nd.append(newUrl)
		yield Request(newUrl,callback=self.parse_3rd_degree_space)
	

    def parse_3rd_degree_space(self,response):
	fn = self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
	    f.write(response.body)
	f.close()
	links = response.xpath('//*[@href]/@href')
	for link in links.extract():
	    newUrl = urlparse.urljoin(response.url,link)		
	    if newUrl not in self.Space_2nd and newUrl not in self.Space_1st and newUrl not in self.Space_3rd:
	        self.Space_3rd.append(newUrl)
		yield Request(newUrl,callback=self.parse_extreme_space)

    def parse_extreme_space(self,response):
	fn = self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
	    f.write(response.body)
	f.close()

    def closed(self,reason):
	print "***************************************************************************"
	print "length of 1st space is %d" %(len(self.Space_1st))
	print self.Space_1st
	print "length of 2nd space is %d" %(len(self.Space_2nd))
	print self.Space_2nd
	print "length of 3rd space is %d" %(len(self.Space_3rd))
	print self.Space_3rd
	print "***************************************************************************"
