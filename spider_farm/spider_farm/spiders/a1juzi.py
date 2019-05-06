# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class A1juziSpider(CrawlSpider):
    custom_settings={
        'DOWNLOAD_DELAY':0.01,
        "FEED_EXPORT_ENCODING":'utf-8', # 保证json输出不是默认的safe numeric encoding(\uXXX序列), http://doc.scrapy.org/en/master/topics/feed-exports.html#feed-export-encoding
    }
    name = '1juzi'
    allowed_domains = ['1juzi.com']
    start_urls = ['http://1juzi.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/new/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title']= re.sub('^\d、','',response.xpath('//*[@id="article"]/h1/text()').extract_first())
        i['sentences']= response.xpath('//*[@id="article"]/div[2]/p/text()').extract()
        return i
