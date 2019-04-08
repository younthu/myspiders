# myspiders
这个库用来记录所有我开发过的或者使用过的爬虫，以及踩过的坑.


## scrapy基本命令

命令 | 解释
-----|-----
scrapy startproject | 创建一个爬虫项目
scrapy genspider <爬虫名> <domain> | 创建spider
scrapy genspider -t crawl <爬虫名> <domain> | 创建crawler
scrapy list | 查看工程里面有哪些爬虫
scrapy view www.baidu.com | 查看爬取的页面在浏览器里面的样子
scrapy crawl spidername | 运行爬虫, 需要在爬虫项目下进行
scrapy runspider spiderfile.py | 运行爬虫, 不需要爬虫项目，只要有爬虫定义文件就可以了
scrapy shell <url> | 爬取一个页面然后进入调试命令行
response.xpath('//*[@id="kkpager"]/div/span/a/@href').extract() | 获取页面链接url
response.xpath('//*[@id="kkpager"]/div/span/a/@href').extract_first() | 获取第一个链接url


## 联系我
给我加星，然后给我发邮件吧.