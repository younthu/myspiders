# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WenzhaihuiSpider(CrawlSpider):
    name = 'wenzhaihui'
    allowed_domains = ['wenzhaihui.com']
    start_urls = ['http://wenzhaihui.com/']

    custom_settings={
        "FEED_EXPORT_ENCODING":'utf-8', # 保证json输出不是默认的safe numeric encoding(\uXXX序列), http://doc.scrapy.org/en/master/topics/feed-exports.html#feed-export-encoding
        }
    rules = (
        Rule(LinkExtractor(allow=r'/xiaohua/.*/.*/'), callback='parse_xiaohua', follow=True),
        Rule(LinkExtractor(allow=r'/lizhi/.*/.*/'), callback='parse_lizhi', follow=True),
        Rule(LinkExtractor(allow=r'/duanxin/.*/.*/'), callback='parse_duanxin', follow=True),
        Rule(LinkExtractor(allow=r'/jingbianzhuanti/.*/.*/'), callback='parse_wenzhai', follow=True),
        Rule(LinkExtractor(allow=r'/shenhuifu/.*/.*/'), callback='parse_shenhuifu', follow=True),
        Rule(LinkExtractor(allow=r'/haojuzi/.*/.*/'), callback='parse_haojuzi', follow=True),
    )

    # 解析pre文本
    def split_list(self, texts):
        # print("XXXXXXXXXXXXXXX\n" + str(texts))
        sentences = []
        sentence = None

        for t in texts:
            if re.search('^\s*\d+、', t):
                if sentence:
                    sentences.append(sentence)
                sentence = re.sub(r"^\s*\d+、",'', t)
                sentence = re.sub(r"\s+$",'', sentence) # 去除末尾空格
            else:
                if sentence: # 跳过没有标号的文本. 有链接中第一行文本为文章标题， http://www.wenzhaihui.com/xiaohua/youmoxiaohua/2018-10-30/17281.html
                    sentence = re.sub(r"\s+$",'', sentence) # 去除末尾空格
                    sentence = sentence + "\n" + t
        
        if sentence:
            sentences.append(sentence)
        
        if len(sentences) == 0: # 解析失败，直接返回texts
            return texts
        return sentences;
                

    def parse_xiaohua(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['origin_text'] = response.xpath('//pre/p/text()').extract()
        i['url'] = response.url
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "笑话"
        return i
    
    def parse_lizhi(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['url'] = response.url
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "励志"
        return i

    def parse_duanxin(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['url'] = response.url
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "短信"
        return i
    
    def parse_meiwen(self, response):
        i={}
        return i
    
    def parse_wenzhai(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['url'] = response.url
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "文摘"
        return i

    def parse_juzimi(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        # i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        return i

    def parse_jiaoyu(self, response):
        i = {}
        return i
    
    def parse_qiushi(self, response):
        i = {}
        return i
    
    def parse_shenhuifu(self, response):
        i = {}
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "神回复"
        return i
    
    def parse_haojuzi(self, response):
        i = {}
        i['title'] = response.xpath('//ul/div[1]/text()').extract_first()
        i['url'] = response.url
        i['sentences'] = self.split_list(response.xpath('//pre/p/text()').extract())
        i['category'] = "好句子"
        return i

    def parse_miyu(self, response):
        i = {}
        return i
    
    def parse_xiehouyu(self, response):
        i = {}
        return i
    
    def parse_naojinjizhuanwan(self, response):
        i = {}
        return i