# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    pass

class CnblogsItem(scrapy.Item):
    name            = scrapy.Field()
    author          = scrapy.Field()
    publish_time    = scrapy.Field()
    rec_count       = scrapy.Field()
    comment_count   = scrapy.Field()
    read_count      = scrapy.Field()
    url             = scrapy.Field()

