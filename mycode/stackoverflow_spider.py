import scrapy
import urlparse
class StackOverflowSpider(scrapy.Spider):
	name = 'stackoverflow'
	start_urls = ['http://stackoverflow.com/questions?sort=votes']
		
	def parse(self, response):
		for href in response.xpath('//*[@class="question-hyperlink"]/@href').extract():
			full_url=urlparse.urljoin(response.url,href)
			yield scrapy.Request(full_url,callback=self.parse_question)
		

	def parse_question(self, response):
		yield {
			'title': response.css('h1 a::text').extract()[0],
			'votes': response.css('.question .vote-count-post::text').extract()[0],
			'body': response.css('.question .post-text').extract()[0],
			'tags': response.css('.question .post-tag::text').extract(),
			'link': response.url,
		}
