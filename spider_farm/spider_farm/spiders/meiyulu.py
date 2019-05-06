# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MeiyuluSpider(CrawlSpider):
    name = 'meiyulu'
    allowed_domains = ['meiyulu.com']
    start_urls = ['http://meiyulu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/sgyl/.*/'), callback='parse_sgyl', follow=True),
    )

    def parse_sgyl(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title']=response.xpath('//div/h1/text()').extract_first()
        nodes = response.xpath('//div[@class="mainbox"]//div[@class="text"]/div')
        sentences = []
        for node in nodes:
            sentence = node.xpath('string(.)').extract_first() # 获取当前节点下所有节点的文本
            sentence = re.sub('^\r\n','',sentence)
            sentence = re.sub('^\s+','', sentence)

            if len(sentence) > 0:
                sentences.append(sentence)
        
        i['sentences'] = sentences

        return i
