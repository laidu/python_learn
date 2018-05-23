#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
if_branch$.py

$ .

Usage:

python3 if_branch$.py $ .
'''

if __name__ == '__main__':

    user_input = int(input('请输入数值：'))
    max_int = 100
    min_int = 1

    if user_input < min_int:
        print('low')
    elif min_int < user_input <= max_int:
        print('mid')
    else:
        print('hight')
