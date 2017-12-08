# -*- coding: utf-8 -*-
import scrapy


class CnblogsspiderSpider(scrapy.Spider):
    name = 'cnblogsSpider'
    allowed_domains = ['https://www.cnblogs.com/']
    start_urls = ['http://https://www.cnblogs.com//']

    def parse(self, response):
        pass
