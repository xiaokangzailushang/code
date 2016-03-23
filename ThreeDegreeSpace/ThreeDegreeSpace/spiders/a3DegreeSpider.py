# -*- coding: utf-8 -*-
import scrapy


class A3degreespiderSpider(scrapy.Spider):
    name = "3DegreeSpider"
    allowed_domains = ["web"]
    start_urls = (
        'http://www.web/',
    )

    def parse(self, response):
        pass
