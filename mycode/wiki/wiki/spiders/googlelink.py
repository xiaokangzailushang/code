# -*- coding: utf-8 -*-
import scrapy
from wiki.items import WikiItem
import urlparse
from selenium import webdriver
from scrapy.http import Request
import time

#driver=webdriver.Firefox()

class GooglelinkSpider(scrapy.Spider):
    name = "googlelink"
    allowed_domains = ["chemistwarehouse.com.au"]
    start_urls=()

    search_word="swisse"

    def __init__(self):
        self.driver = webdriver.Firefox()
        #driver.get('http://www.google.com/ncr')
        self.driver.get('http://www.chemistwarehouse.com.au/home.aspx')
        time.sleep(4)
        button=self.driver.find_element_by_xpath('//a[@class="pp_close"]')
        button.click()
        inputElement=self.driver.find_element_by_xpath('//input[@type="text"]')
        #inputElement=driver.find_element_by_name("q")
        inputElement.send_keys(self.search_word)
        button2=self.driver.find_element_by_xpath('//input[@class="SearchBTN"]')
        button2.click()
        #inputElement.submit()
        self.start_urls =(self.driver.current_url,) + self.start_urls
        time.sleep(4)

    def parse(self,response):
        #next_page = response.xpath('//a[@class="pn"]/@href').extract()
        #next_page = urlparse.urljoin(response.url,next_page)
        try:
            """time.sleep(4)
            next_page = driver.find_element_by_xpath('//a[@id="pnnext"]')
            yield Request(driver.current_url,callback=self.parse_item)
            next_page.click()
            print "-----------------------------------------------------"
            print driver.current_url
            print "-----------------------------------------------------"
            time.sleep(4)
            #yield Request("http://www.baidu.com")"""
            next_page = self.driver.find_element_by_xpath('//a[text()="Next"')[0]
            next_page.click()

        finally:
            pass




    def parse_item(self, response):
        links = response.xpath('//h3[@class="r"]/a[@href]/@href').extract()
        for link in links:
            qs=urlparse.urlparse(link).query
            link = urlparse.parse_qs(qs).get('q',[])
            print '******************************************************'
            print link
            print '******************************************************'

