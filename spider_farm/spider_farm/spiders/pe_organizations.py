# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from spider_farm.items import PEOrganizationItem


class PeOrganizationsSpider(scrapy.Spider):
    """ scrapy org.pedata.cn's company name
    爬取pedata.cn的PE机构名称.

    使用方法:
    1. 在../../目录下运行下面的命令，结果会自动保存到result.csv文件里:
    scrapy crawl pe_organizations -o result.csv

    注意事项:
    1. ROBOTSTXT_OBEY 设置为False, 否则爬虫会因为网站不允许robots爬取而放弃爬取内容。
    2. DOWLOAD_DELAY设置为1或者更大，否则会被网站发现然后返回302，跳转到列表页面，爬取失败.
    """

    # settings list: http://doc.scrapy.org/en/latest/topics/settings.html
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        "DOWNLOAD_DELAY": 1
    }

    name = 'pe_organizations'
    allowed_domains = ['org.pedata.cn']
    start_urls = ['https://org.pedata.cn/list_{}_0_0_0_0_0.html'.format(i) for i in range(1,1501)]

    def parse(self, response):
        full_names=response.xpath('//*[@id="org_info_table"]/tr/td[1]/a/text()').extract()
        company_pages=response.xpath('//table[@id="org_info_table"]/tr/td/a/@href').extract()

        # dump full_names to pe_org_full_names.txt
        with open('pe_org_full_names.txt', 'a') as f:
            for name in full_names:
                f.write(name+","+response.url+"\n")

        for company in company_pages:
            print(company)
            req=Request(company,callback=self.parse_company_details)
            yield req
        pass

    def parse_company_details(self, response):
        full_name=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/text()').extract_first()
        short_name=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/text()[contains(.,"机构简称")]').extract_first()
        created_at=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]/text()').extract_first()
        header_quater=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/ul/li[3]/text()').extract_first()
        capital_type=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/ul/li[4]/text()').extract_first()
        capital_size=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[1]/ul/li[5]/text()').extract_first()

        contact_address=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/text()').extract_first()
        zip_code=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/text()').extract_first()

        contact_person=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/text()').extract_first()
        contact_email=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/text()').extract_first()

        contact_phone=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/text()').extract_first()
        contact_fax=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/text()').extract_first()

        org_description=response.xpath('//*[@id="pedetamain"]/div[2]/div[1]/div[1]/div[4]/p/text()').extract_first()

        item = PEOrganizationItem({
            "full_name": full_name,
            "short_name":short_name,
            "created_at":created_at,
            "header_quater": header_quater,
            "capital_type": capital_type,
            "capital_size": capital_size,
            "contact_address": contact_address,
            "zip_code": zip_code,
            "contact_person": contact_person,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "contact_fax": contact_fax,
            "org_description": org_description
        })
        return item;
