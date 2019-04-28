# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderFarmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PEOrganizationItem(scrapy.Item):
    full_name= scrapy.Field()
    short_name=scrapy.Field()
    created_at=scrapy.Field()
    header_quater=scrapy.Field()
    capital_type=scrapy.Field()
    capital_size=scrapy.Field()

    contact_address=scrapy.Field()
    zip_code=scrapy.Field()

    contact_person=scrapy.Field()
    contact_email=scrapy.Field()
    contact_phone=scrapy.Field()
    contact_fax=scrapy.Field()

    org_description=scrapy.Field()
