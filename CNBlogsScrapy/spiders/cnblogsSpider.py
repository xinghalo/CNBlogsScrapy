# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import scrapy
from CNBlogsScrapy.items import CnblogsItem

class CnblogsspiderSpider(scrapy.Spider):
    name = 'cnblogsSpider'
    allowed_domains = ['www.cnblogs.com/']
    #start_urls = ['https://www.cnblogs.com/']

    def start_requests(self):
        for i in range(1,10):
            url = "http://www.cnblogs.com/mvc/AggSite/PostList.aspx?CategoryType=SiteHome&ParentCategoryId=0&CategoryId=808&PageIndex="+str(i)+"&ItemListActionName=PostList"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for blog in response.xpath('//div[@class="post_item"]'):
            item = CnblogsItem()

            item['name'] = blog.xpath('./div[@class="post_item_body"]/h3/a/text()').extract_first().decode("utf-8")
            item['author'] = blog.xpath('./div[@class="post_item_body"]/div/a/text()').extract_first().decode("utf-8")
            # 这个时间有点问题
            #item['publish_time'] = blog.xpath('./div[@class="post_item_body"]/div[@class="post_item_foot"]/text()').extract_first().decode("utf-8")
            item['rec_count'] = blog.xpath('./div[@class="digg"]/div[@class="diggit"]/span[@class="diggnum"]/text()').extract_first().decode("utf-8")
            item['comment_count'] = blog.xpath('./div[@class="post_item_body"]/div/span[1]/a/text()').extract_first().decode("utf-8")
            item['read_count'] = blog.xpath('./div[@class="post_item_body"]/div/span[2]/a/text()').extract_first().decode("utf-8")
            item['url'] = blog.xpath('./div[@class="post_item_body"]/h3/a/@href').extract_first().decode("utf-8")

            yield item

