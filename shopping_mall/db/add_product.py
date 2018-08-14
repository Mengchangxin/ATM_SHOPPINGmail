#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
用来生成商品测试数据
Administrator 
2018/8/14 
'''
import os,sys,logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
from conf import settings

product_list={
    "1":{'iphone6s':5800},
    "2":{'mac book':9000,},
    "3":{'coffee':32},
    "4":{'python book':80},
    "5":{'bicyle':1500},
    "6":{'football':100}

}
files=settings.db_file
def save_db(data):
    with open(files,"w") as f:
        json.dump(data,f)

if __name__=="__main__":
    save_db(product_list)
