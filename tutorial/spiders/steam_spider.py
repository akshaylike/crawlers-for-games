from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from tutorial.items import ResultItem

class SteamSpider(BaseSpider):
	name = "steam_results"
	allowed_domains = ["store.steampowered.com"]

	start_urls = ["http://store.steampowered.com/search/?snr=1_4_4__12&term=all#sort_by=&sort_order=ASC&page=%d" % (n) for n in range(1,6)]

	def parse(self, response):
		sel = Selector(response)

		#Container to hold entire search result container
		#resultsContainer = sel.xpath('//div[@id="search_result_container"]')
		#Container to hold results themselves
		results = sel.xpath('//div[@id="search_results"]/div[@id="search_result_container"]/div[6]/a')
		
		pagination = sel.xpath('//div[@class="search_pagination_right"]/a')
		resultItems = []

		for each in results:
			item = ResultItem()
			item['link'] = each.xpath('@href').extract()
			item['title'] = each.xpath('div[@class="col search_name ellipsis"]/h4/text()').extract()
			resultItems.append(item)
		return resultItems
