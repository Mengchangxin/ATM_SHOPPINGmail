#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/14 
'''
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
import logging
from conf import settings
# level=logging.WARNING#可以把这个放在配置文件中
def logger(log_type):
    logger=logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file=r"%s\log\%s"%(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    fh=logging.FileHandler(log_file+'.log')
    #ch=logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    #ch.setFormatter(formatter)
    logger.addHandler(fh)
    #logger.addHandler(ch)

    return logger


if __name__=='__main__':
    logger('test_logger').warning('logger debug message')
    # print(log_file)