from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector

from game_spiders.items import ResultItem

class GMGSpider(BaseSpider):
	name = "gmg_results"
	allowed_domains = ["www.greenmangaming.com"]

	def start_requests(self):
		return [Request("http://www.greenmangaming.com/s/in/en/pc/games/", callback=self.parse_initial)]

	def parse_initial(self, response):
		sel = Selector(response)
		url = "http://www.greenmangaming.com/s/in/en/pc/games/?page="

		numberOfPages = int(sel.xpath('//div[@class="paginator"]/a[@title="Last page"]/text()').extract()[0])
		
		for page in range(1, numberOfPages+1):
			final_url = url + str(page)
			yield Request(final_url, callback=self.parse_pages)	

	def parse_pages(self, response):
		sel = Selector(response)

		resultItems = []
		results = sel.xpath('//ul[@class="product-list"]/li')

		for each in results:
			item = ResultItem()
			item['link'] = each.xpath('a/@href').extract()
			item['title'] = each.xpath('h2/text()').extract()
			resultItems.append(item)

		return resultItems
