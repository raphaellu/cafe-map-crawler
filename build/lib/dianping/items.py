# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    num_comment = scrapy.Field()
    price = scrapy.Field()
    dish_type = scrapy.Field()
    area = scrapy.Field()
    addr = scrapy.Field()
    flavor_rate = scrapy.Field()
    env_rate = scrapy.Field()
    srv_rate = scrapy.Field()
   