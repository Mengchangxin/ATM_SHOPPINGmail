#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/8/12
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)
from core import db_handler
from conf import setting
from core import logger
import json,time


def load_current_balance(account_id):
    db_path = db_handler.db_handler(setting.DATABASE)  # 返回的是数据文件路径
    account_file = "%s/%s.json" % (db_path, account_id)  # 取到数据文件的绝对地址
    with open(account_file, "r") as f:
        account_data = json.load(f)
        return account_data