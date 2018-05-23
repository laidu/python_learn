#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
double_format$.py

$ .

Usage:

python3 double_format$.py $ .
'''

if __name__ == '__main__':

    double_format = '%.2f'
    result = 1000 / 3
    print(double_format % result)
