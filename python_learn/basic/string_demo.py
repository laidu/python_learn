#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
string_demo.py

$ .

Usage:

python3 string_demo$.py $ .
'''

if __name__ == '__main__':
    aa = 'hello world'
    print(aa)

    aa = '你好'
    print(aa.encode('utf-8'))

    print(len(aa))

    # 字符串格式化
    template = 'Hello, %s !'
    print(template % "xiaoming")
    print(template % "xiaoli")

    # 使用 format 方法格式化
    template = '今天是 {0} 年 {1} 月 {2} 日'
    print(template.format('2018', '6', '1'))
