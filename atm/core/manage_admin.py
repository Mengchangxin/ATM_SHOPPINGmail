#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/8/12

#管理端(提供管理接口，包括添加账户、用户额度，冻结账户)
#解冻账户
#from core.auth import login_required
from core import accounts
from core import transaction

#解冻账户
def unblock_account():
    user_input = input("请输入你要解冻的用户：")
    flag = 0
    #锁定用户
    val = transaction.unlock_or_yes(user_input,flag)
    if val == 0:
        print("解冻成功！")
        return
#冻结账户
def block_account():
    '''
    冻结账户初步构想是，在linux里把他的权限改掉;
    或者将其文件改名
    :param acc_data:
    :return:
    '''
    user_input = input("请输入你要冻结的用户：")
    flag = 1
    #锁定用户
    val = transaction.lock_or_not(user_input,flag)
    if val == 1:
        print("冻结成功！")
        return
#添加账户、用户额度
def add_account():
    account = {
        "id": None,
        "balance": None,
        "expir_date": None,
        "enroll_date": None,
        "credit": None,
        "pay_day": None,
        "password": None,
        "status": 0,
        "role":1
    }
    menu = {
        0: "账户（数字）:",
        1: "密码:",
        2: "信用额度:",
        3: "余额度:",
        4: "注册时间:",
        5: "到期时间:",
        6: "还款周期:",
        7: "默认(0 正常  1 锁卡 2  遗失):",
        8:"权限（0 管理员，1用户。默认用户1）："
         }
    menu_user = {
        0: "id",
        1: "password",
        2: "credit",
        3: "balance",
        4: "enroll_date",
        5: "expir_date",
        6: "pay_day",
        7: "status",
        8:"role"
    }
    for i in range(7):
        data = input("%s" % menu[i]).strip()
        account['%s' % menu_user[i]] = data

    account["balance"]=float(account["balance"] )
    accounts.dump_account(account)#写入文件
    print("创建成功！")
    return
def logout():
    exit("程序退出！")
#管理界面主程序
def manage_main():

    menu = u'''
    ---------管理界面---------
    1.添加账户
    2.冻结账户
    3.解冻账户
    4.退出'''
    menu_dic = {
        '1': add_account,
        '2': block_account,
        '3': unblock_account,
        '4': logout
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input("请输入你的选择：")
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("\033[31;1m选择不存在！\033[0m")

if __name__=="__main__":
    #manage_main()
    pass