# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        pass


class AppPipeline(object):
    def process_item(self, item, spider):
        file_path = '/home/laidu/Downloads/app/' + item['app_name'] + '/'
        app_download_url = item['app_download_url']
        app_file_name = file_path + item['app_pkg_name'] + '.apk'

        if not os.path.exists(app_file_name):
            self.dir_check(file_path)
            f = requests.get(app_download_url)

            with open(app_file_name, "wb") as code:
                code.write(f.content)

        return item

    def dir_check(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
