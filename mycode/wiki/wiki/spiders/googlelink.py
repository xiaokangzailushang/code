# -*- coding: utf-8 -*-
import scrapy
from wiki.items import WikiItem
import urlparse


class GooglelinkSpider(scrapy.Spider):
    name = "googlelink"
    allowed_domains = ["google.com"]
    start_urls = (
        #'https://www.google.com/#q=anu',
        'https://www.google.com.au/search?site=&source=hp&q=anu&oq=anu&gs_l=hp.3..0i131l3j0l7.1145.1606.0.1894.3.3.0.0.0.0.214.590.0j2j1.3.0....0...1c.1j4.64.hp..0.3.589.iYl0RdfH9k8',
    )

    def parse(self,response):
        next_page = response.xpath('//a[@class="pn"]/@href').extract()
        next_page = urlparse.urljoin(response.url,next_page)
        print '------------------------------------'
        print next_page
        print '------------------------------------'

    def parse_item(self, response):
        links = response.xpath('//h3[@class="r"]/a[@href]/@href').extract()
        for link in links:
            qs=urlparse.urlparse(link).query
            link = urlparse.parse_qs(qs).get('q',[])
            print '--------------------------------------------------'
            print link
            print '---------------------------------------------------'

