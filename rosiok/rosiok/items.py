# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RosiokItem(scrapy.Item):
    img_url = scrapy.Field()
    image_paths = scrapy.Field()
