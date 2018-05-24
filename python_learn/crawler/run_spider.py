#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
run_spider$.py

$ .

Usage:

python3 run_spider$.py $ .
'''

from scrapy import cmdline

cmdline.execute("scrapy crawl yingyongbao".split())
