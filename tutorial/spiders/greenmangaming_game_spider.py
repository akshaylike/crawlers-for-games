from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector

from tutorial.items import GmgGameItem
import json

class GMGGameSpider(BaseSpider):
	name = "greenmangaming_game_spider"
	allowed_domains = ["www.greenmangaming.com"]

	base_url = "http://www.greenmangaming.com"
	games_list = json.load(open("gmgitems.json"))

	def start_requests(self):
		for game in self.games_list:
			yield Request(self.base_url+game['link'][0], callback=self.parse_game_data)

	def parse_game_data(self, response):
		gameItem = GmgGameItem()
		selector = Selector(response)

		gameItem['gameTitle'] = selector.xpath('//div[@class="wrapper"]/h1[@class="prod_t"]/text()').extract()
		gameItem['gameLink'] = response.url

		gameItem['onSale'] = str(selector.xpath('boolean(//span[@class="lt"])'))

		if gameItem['onSale']:
			gameItem['rrp'] = selector.xpath('//span[@class="lt"]/text()').extract()
			gameItem['drp'] = selector.xpath('//strong[@class="curPrice"]/text()').extract()
		else:
			gameItem['rrp'] = selector.xpath('//strong[@class="curPrice"]/text()').extract()

		gameItem['steamworks'] = str(selector.xpath('boolean(//a[@id="steam"])'))

		return gameItem

