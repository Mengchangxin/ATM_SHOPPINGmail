#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/14 
'''
import os,sys,logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_file=os.path.join(BASE_DIR,"db","access","produc.json")

LOG_TYPES = {
    'shopping': 'shopping.log',
}
LOG_LEVEL = logging.INFO  #记录等级
DATABASE = {
        'engine': 'file_storage',
        'name': 'access',
        "file":"produc.json",
        'path': "%s/db" % BASE_DIR
}




if __name__=="__main__":
        print(BASE_DIR)
        print(db_file)