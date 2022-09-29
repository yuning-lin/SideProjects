# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    period = scrapy.Field()
    lottery_date = scrapy.Field()
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    num3 = scrapy.Field()
    sales_amt = scrapy.Field()
    deadline_date = scrapy.Field()
    prize1 = scrapy.Field()
    prize2 = scrapy.Field()
    prize3 = scrapy.Field()
    prize4 = scrapy.Field()
    prize_amt = scrapy.Field()
