#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/14 
'''
import os,sys,logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def file_db_handle(conn_params):
    db_path=os.path.join(conn_params["path"],conn_params["name"],conn_params["file"])
    return db_path

def mysql_db_handle(conn_parms):
    pass

def db_handler(conn_parms):
    "链接数据文件"
    if conn_parms["engine"]=="file_storage":
        return file_db_handle(conn_parms)
    elif conn_parms["engine"]=="mysql":
        return mysql_db_handle(conn_parms)