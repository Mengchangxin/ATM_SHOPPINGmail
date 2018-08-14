#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/14 
'''
import os,sys,logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from core import db_handler
import json

#取数据
def load_current_balance():
    db_file_path = db_handler.db_handler(settings.DATABASE)  # 返回的是数据文件路径# 取到数据文件的绝对地址
    with open(db_file_path, "r") as f:
        account_data = json.load(f)
        return account_data


#存数据
def dump_account(account_data):
    db_file_path = db_handler.db_handler(settings.DATABASE)  # 返回的是数据文件路径 # 取到数据文件的绝对地址
    with open(db_file_path,"w") as f:
        json.dump(account_data,f)
    return True
