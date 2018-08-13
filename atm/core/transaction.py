#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/8/12
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)
from conf import setting
from core import accounts

def make_transaction(log_obj,account_data,tran_type,amount,**kwargs):
    amount=float(amount)
    if tran_type in setting.TRANSACTION_TYPE:
        interest=amount*setting.TRANSACTION_TYPE[tran_type]["interest"]#计算利息
        old_balance=account_data["balance"]
        if setting.TRANSACTION_TYPE[tran_type]["action"]=="plus":
            new_balance=old_balance+amount+interest
        elif setting.TRANSACTION_TYPE[tran_type]["action"]=="minus":
            new_balance=old_balance-amount-interest
            if new_balance<0:
                print("\033[31;1m[%s]账户的信用余额不足以支付此次交易[-%s]，你当前的余额是[%s]\033[0m"%(
                    account_data['id'],amount+interest,old_balance))
                return None
        account_data["balance"]=new_balance
        accounts.dump_account(account_data)#保存数据
        log_obj.info("account:%s action:%s   amount:%s    interest:%s "%(account_data['id'],tran_type,amount,interest))
        return account_data  #返回最新数据
    else:
        print("\033[31;1m交易类型【%s】 is not exist!!!\033[0m"%tran_type)


