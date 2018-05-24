# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AppIterm(scrapy.Item):
    app_name = scrapy.Field()
    app_download_url = scrapy.Field()
    app_pkg_name = scrapy.Field()
    app_md5 = scrapy.Field()
