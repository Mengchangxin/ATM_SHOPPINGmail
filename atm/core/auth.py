#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)
from core import db_handler
from conf import setting
from core import logger
import json,time,functools


#做一个登陆装饰器
def login_required(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("用户认证失败")
    return wrapper


#第二步，做一个用户认证功能
#初始化信息，一旦认证成功，就把数据传给这个字典

#输入账户id 和密码
def acc_auth(account,password):
    db_path=db_handler.db_handler(setting.DATABASE)#返回的是数据文件路径
    account_file="%s/%s.json"%(db_path,account)#取到数据文件的绝对地址
    #print(account_file)                                   #打印一下地址
    if os.path.isfile(account_file):
        with open(account_file,"r") as f:
            account_data=json.load(f)
            if account_data["password"]==password:
                exp_time_stamp=time.mktime(time.strptime(account_data["expir_date"],'%Y-%m-%d'))
                if time.time()>exp_time_stamp:
                    print("\033[32;1m账户%s已经过期，请联系管理人处理。：\033[0m"%account)
                else:
                    return account_data
            else:
                print("\033[32;1m账户或密码，存在错误。\033[0m")

def acc_login(user_data,log_obj):#用户验证函数
    retry_count=0
    while user_data["is_authenticated"] is not True and retry_count<3:
        account=input("\033[32;1m账户：\033[0m").strip()
        password = input("\033[32;1m密码：\033[0m").strip()
        auth=acc_auth(account,password) #调用登陆函数
        if auth:
            user_data["is_authenticated"]=True
            user_data["account_id"]=account
            log_obj.info("账户 %s 登陆登陆成功"%account)
            return auth
        retry_count+=1
    else:
        log_obj.error("账户 %s 多次尝试登陆"%account)#打印一个登陆信息
        exit()#退出登录程序
