# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request
import re

class ThreedegreespiderSpider(scrapy.Spider):
    name = "ThreeDegreeSpider"
    allowed_domains = []
    start_urls = (
        'http://example.webscraping.com',
    )
    Space_1st=[]
    Space_2nd=[]
    Space_3rd=[]
    pattern = re.compile(r"/+")
    pattern_url = re.compile(r"http")

    def parse(self, response):
        fn = "google_output"
	f = open(fn)
	
	while True:
	    line = f.readline()
	    if len(line) == 0:
		break
	    if not self.pattern_url.match(line):
		line = 'http://' + line
	    line = line.strip('\n')
	    if line not in self.Space_1st:
		self.Space_1st.append(line)
	        print line
	        yield Request(line,callback=self.parse_2nd_degree_space)
	f.close()

    def parse_2nd_degree_space(self,response):
	fn = "./page_save/" + self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
            f.write(response.body)
	    #texts = response.xpath('//*/text()')
            #for text in texts:
            #    f.write(text.extract())
	f.close()
	links = response.xpath('//*[@href]/@href')
	for link in links.extract():
	    newUrl = urlparse.urljoin(response.url,link)		
	    if newUrl not in self.Space_2nd and newUrl not in self.Space_1st:
	        self.Space_2nd.append(newUrl)
		yield Request(newUrl,callback=self.parse_3rd_degree_space)
	

    def parse_3rd_degree_space(self,response):
	fn = "./page_save/" + self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
	    f.write(response.body)
	    #texts = response.xpath('//*/text()')
            #for text in texts:
            #    f.write(text.extract())
	f.close()
	links = response.xpath('//*[@href]/@href')
	for link in links.extract():
	    newUrl = urlparse.urljoin(response.url,link)		
	    if newUrl not in self.Space_2nd and newUrl not in self.Space_1st and newUrl not in self.Space_3rd:
	        self.Space_3rd.append(newUrl)
		yield Request(newUrl,callback=self.parse_extreme_space)

    def parse_extreme_space(self,response):
	fn = "./page_save/" + self.pattern.sub('_',response.url)
	with open(fn,'w') as f:
	    f.write(response.body)
	    #texts = response.xpath('//*/text()')
            #for text in texts:
            #    f.write(text.extract())
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
