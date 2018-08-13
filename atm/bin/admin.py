#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/13 
'''
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
sys.path.append(BASE_DIR)

from core import main


if __name__ == '__main__':
    main.goto_manage()