# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # fields defined for the items container
    # this items.py should be imported in the quotes_spider.py file
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

