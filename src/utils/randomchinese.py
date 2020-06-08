#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# unicode 简体字跟繁体字都有
def get_random_char(number):
    val_list = []
    for nu in range(0, number):
        val_list.append(chr(random.randint(0x4e00, 0x9fbf)))
    return "".join(val_list)

# gbk2312 常见的简体字
def get_random_char1(length):
    val_list = []
    for c in range(0, length):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x}{body:x}'
        str_var = bytes.fromhex(val).decode('gb2312')
        val_list.append(str_var)
    return "".join(val_list)

