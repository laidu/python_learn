# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request

from ..items import AppIterm

'''
http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=114&pageSize=20&pageContext=82
'''
page_context = 0
category_id = 114
page_size = 40


class YingyongbaoSpider(scrapy.Spider):

    name = 'yingyongbao'
    allowed_domains = ['sj.qq.com']

    crawler_url = 'http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId={0}&pageSize={1}&pageContext={2}' \
        .format(category_id, page_size, page_context)

    start_urls = [crawler_url]

    def parse(self, response):
        global page_context
        result = json.loads(response.body_as_unicode())
        if result['count'] != 0 and result['obj'] is not None:
            app_items = result['obj']
            for app_item in app_items:
                app = AppIterm()
                app['app_download_url'] = app_item['apkUrl']
                app['app_name'] = app_item['appName']
                app['app_pkg_name'] = app_item['pkgName']
                app['app_md5'] = app_item['apkMd5']
                yield app
            page_context += 1
            yield Request(url=self.crawler_url)
