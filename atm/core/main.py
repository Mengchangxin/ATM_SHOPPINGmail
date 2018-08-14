#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
sys.path.append(BASE_DIR)



from core import auth
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
from core import manage_admin
import time


user_data={
    'account_id':None,#账号id
    'is_authenticated':False, #是否认证
    'account_data':None #账户其他数据
}

trans_logger=logger.logger('transaction') #交易logger
access_logger=logger.logger('access')      #登录logger



@login_required
def account_info(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = """
        ------卡   基本信息 ---------
        卡号:        %s
        信用额度：    %s
        可用额度:    %s
        开卡时间：   %s
        过期时间：   %s
        """ % (account_data['id'],account_data["credit"], account_data['balance'],account_data["enroll_date"],account_data["expir_date"])
    print(current_balance)
@login_required
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
        repay_amount=input("\033[33;1m输入你要还款的金额：[放弃：q]\033[0m").strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
            new_blance=transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)#交易完成后得到最新数据
            if new_blance:
                print("\033[33;1m最新余额：%s\033[0m"%new_blance["balance"])
        elif repay_amount=="q":
            back_flag=True
        else:
            print("\033[33;1m[%s] is not a valid amount,only accept integer!!\033[0m"%repay_amount)
@login_required
def withdraw(acc_data):#取款
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = """
       ------balance 余额 INFO ---------
       Credit:     %s
       Balance:    %s
       """ % (account_data['id'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1m输入你要取款的金额：[放弃：q]\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_blance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)  # 交易完成后得到最新数据
            if new_blance:
                print("\033[33;1m最新余额：%s\033[0m" % new_blance["balance"])
        elif withdraw_amount == "q":
            back_flag = True
        else:
            print("\033[33;1m 账户或输入金额 is not a valid amount!\033[0m")
@login_required
def transfer(acc_data): #4、转账
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = """
          ------balance 余额 INFO ---------
          Credit:     %s
          Balance:    %s
          """ % (account_data['id'], account_data['balance'])
    print(current_balance)
    back_flag=False
    while not back_flag:
        duifang_account=input("\033[31;1m请输入对方帐户名：\033[0m").strip()
        transfer_amount=input("\033[31;1m转账金额：\033[0m").strip()
        if duifang_account and transfer_amount=="b":
            return
        elif len(transfer_amount)>0 and transfer_amount.isdigit():
            new_blance=transaction.make_transaction(trans_logger,account_data,"transfer",transfer_amount,re_account=duifang_account)
            if new_blance:
                print("\033[41;1m转账成功！\033[0m")
                print("\033[33;1m最新余额：%s\033[0m" % new_blance["balance"])
        else:
            print("\033[33;1m 账户或输入金额 is not a valid amount!\033[0m")

@login_required
def pay_check(acc_data):
    pass
@login_required
def logout(acc_data):
    exit("程序已退出")
 #############################################
def shopping_mall_this(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])#取得最新数据
    saving=account_data["balance"]#得到可用额度
    surplus_amount=main.shopping_action(saving)#需要返回 消费的金额
    new_blance = transaction.make_transaction(trans_logger, account_data, 'consume', surplus_amount)  # 交易完成后得到最新数据
    if new_blance:
        print("\033[33;1m最新余额：%s\033[0m" % new_blance["balance"])

###############################################

def goto_manage():
    manage_admin.manage_main()
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
def atm_shoping_menu(acc_data):
    main_menu=u"""
    ----------主菜单---------
     \033[32;1m
     1.购物商城
     2.银行卡操作
     3.退出\033[0m"""
    main_menu_dic={
        "1":shopping_mall_this,
        "2":interactive,
        "3":logout
    }
    exit_flag1=False
    while not exit_flag1:
        print(main_menu)
        user_option=input("请选择：").strip()
        if user_option=="b":
            return
        elif user_option in main_menu_dic:
            main_menu_dic[user_option](acc_data)
        else:
            print("\033[31;1m选择不存在！\033[0m")


def run():
    #首先需要进行用户验证
    acc_data=auth.acc_login(user_data,access_logger)

    if user_data['is_authenticated']: #确认是否验证
        user_data["account_data"]=acc_data
        #interactive(user_data)##把user_data里的所有数据传入菜单函数，进行下一步操作
        #atm_shoping_menu(user_data)#接入商场菜单
        if acc_data["role"]==0 or acc_data["role"]=="0":#role  0 管理员    1是普通用户
            goto_manage()
        if acc_data["role"]==1 or acc_data["role"]=="1":
            atm_shoping_menu(user_data)






if __name__=='__main__':
    run()