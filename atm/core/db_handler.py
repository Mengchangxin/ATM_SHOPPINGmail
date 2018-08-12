#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/8/12


def file_db_handle(conn_params):
    print("file db:",conn_params)
    db_path="%s/%s"%(conn_params["path"],conn_params["name"])
    return db_path

def mysql_db_handle(conn_parms):
    pass

def db_handler(conn_parms):
    "链接数据文件"
    if conn_parms["engine"]=="file_storage":
        return file_db_handle(conn_parms)
    elif conn_parms["engine"]=="mysql":
        return mysql_db_handle(conn_parms)

