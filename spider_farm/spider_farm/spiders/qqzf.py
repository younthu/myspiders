# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QqzfSpider(CrawlSpider):
    custom_settings={
        "FEED_EXPORT_ENCODING":'utf-8', # 保证json输出不是默认的safe numeric encoding(\uXXX序列), http://doc.scrapy.org/en/master/topics/feed-exports.html#feed-export-encoding
        }
    name = 'qqzf'
    allowed_domains = ['qqzf.cn']
    start_urls = ['http://qqzf.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'/.*/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title']=response.xpath('//*[@id="article"]/h1/text()').extract_first()
        i['sentences']=response.xpath('//*[@id="article"]/div[3]/p/text()').extract()
        return i
