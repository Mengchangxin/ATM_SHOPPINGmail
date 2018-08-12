#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/15
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)
import logging
from conf import setting
# level=logging.WARNING#可以把这个放在配置文件中
def logger(log_type):
    logger=logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

    log_file="%s/log/%s"%(setting.BASE_DIR,setting.LOG_TYPES[log_type])
    fh=logging.FileHandler(log_type+'.log')
    ch=logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


if __name__=='__main__':
    logger('test_logger').warning('logger debug message')