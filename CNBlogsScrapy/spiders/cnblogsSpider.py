# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import scrapy
from CNBlogsScrapy.items import CnblogsItem

class CnblogsspiderSpider(scrapy.Spider):
    name = 'cnblogsSpider'
    allowed_domains = ['www.cnblogs.com/']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        for blog in response.xpath('//div[@class="post_item"]'):
            item = CnblogsItem()

            item['name'] = blog.xpath('./div[@class="post_item_body"]/h3/a/text()').extract_first().decode("utf-8")

            yield item

