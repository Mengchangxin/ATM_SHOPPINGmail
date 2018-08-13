#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
sys.path.append(BASE_DIR)

from core import main


if __name__ == '__main__':
    main.run()



