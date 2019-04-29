# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline, MediaPipeline

class RailsCastsVideoItem(scrapy.Item):
    file_urls = scrapy.Field()  # 指定文件下载的连接
    files = scrapy.Field()      #文件下载完成后会往里面写相关的信息, 输出到csv或者数据库

class VideoFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        split_url = str(request.url).split('/')
        file_name = split_url[-1]
        return file_name

class RailscastsSpider(scrapy.Spider):
    """
    下载railscasts.com的所有mp4课程视频.

    使用方法:
    scrapy crawl railscasts #所有视频会下载到railscasts_downloads目录下面去
    """
    name = 'railscasts'
    allowed_domains = ['railscasts.com']
    start_urls = ['http://railscasts.com/']

    custom_settings={
        'ITEM_PIPELINES': {
            #'scrapy.pipelines.files.FilesPipeline':1
            'spider_farm.spiders.railscasts.VideoFilesPipeline': 1
        },
        'FILES_STORE':os.getcwd() + '/railscasts_downloads',
        'DOWNLOAD_DELAY': 1,
    }

    def parse(self, response):
        pages = response.xpath("//div[@id='main']//h2/a/@href").extract()
        lists = response.xpath("//*[@id='main']/div/div[2]/div[2]/a/@href").extract()

        for p in pages:
            req = Request("http://railscasts.com"+p, callback=self.parseVideoPage)
            yield req
        
        for l in lists:
            req = Request("http://railscasts.com"+l)
            yield req
        
    
    def parseVideoPage(self, response):
        videoUrl=response.xpath('//*[@id="episode"]/div[1]/ul/li[3]/a/@href').extract_first()

        videoItem = RailsCastsVideoItem(file_urls = [videoUrl])
        yield videoItem