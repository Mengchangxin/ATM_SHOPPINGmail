#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14
import os,sys
BASE_DIR=os.path.dirname(o.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)
from core import auth
from core import logger
from core import accounts
from core import transaction

user_data={
    'account_id':None,#账号id
    'is_authenticated':False, #是否认证
    'account_data':None #账户其他数据
}

trans_logger=logger.logger('transaction') #交易logger
access_logger=logger.logger('access')      #登录logger
def account_info(acc_data):
    print(user_data)
def repay(acc_data):
    #取出最新的数据，为了保证数据的安全
    account_data=accounts.load_current_balance(acc_data['account_id'])
    current_balance="""
    ------balance 余额 INFO ---------
    Credit:     %s
    Balance:    %s
    """%(account_data['id'],account_data['balance'])
    print(current_balance)
    back_flag=False
    while not back_flag:
        repay_amount=input("\033[33;1m输入你要还款的金额：\033[0m").strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
            new_blance=transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)

def withdraw(data):
    pass
def transfer(data):
    pass
def pay_check():
    pass
def logout():
    pass
def interactive(acc_data):
    menu=u'''
    --------中国银行---------
    \033[32;1m1、账户信息
    2、还款
    3、取款
    4、转账
    5、账单
    6、退出\033[0m'''
    menu_dic={
        "1":account_info, #1、账户信息
        "2":repay,        #2、还款
        "3":withdraw,     #3、取款
        "4":transfer,      #4、转账
        "5":pay_check,    #5、账单
        "6":logout        #6、退出
    }
    exit_flag=False
    while not exit_flag:
        print(menu)
        user_option=input("请选择>>>").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
           print("\033[32;1m您的选择不存在。\033[0m")


def run():
    #首先需要进行用户验证
    acc_data=auth.acc_login(user_data,access_logger)

    if user_data['is_authenticated']: #确认是否验证
        user_data["account_data"]=acc_data
        interactive(user_data)#交互





if __name__=='__main__':
    run()