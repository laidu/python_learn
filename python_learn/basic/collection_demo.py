#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
collection_demo$.py

$ .

Usage:

python3 collection_demo$.py $ .
'''

if __name__ == '__main__':

    # 列表 有序集合，可动态增删元素
    list_int = [1, 2, 34, 45, 54, 12]
    print(list_int)
    print(type(list_int))

    for var in list_int:
        print(var)

    # 直接获取最后一个元素
    print('最后一个元素 %d' % list_int[-1])
    print('倒数第二个元素 %d' % list_int[-2])

    # 元组（数组）
    string_array = ('aaa', 'bbb', 'ccc')
    print(string_array)
