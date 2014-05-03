# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ResultItem(Item):
	link = Field()
	title = Field()

class SteamGameItem(Item):
	def __init__(self, gameTitle, gameLink):
		self.gameTitle = gameTitle
		self.storeId = gameLink.split("/")[-1]
	
	rrp = Field()
	drp = Field()
	platforms = Field()
	saleEndTime = Field()

class GmgGameItem(Item):
	gameTitle = Field()
	gameLink = Field()

	rrp = Field()
	drp = Field()
	onSale = Field()
	steamworks = Field()

