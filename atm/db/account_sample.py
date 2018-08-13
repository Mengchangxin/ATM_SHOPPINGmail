#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14

import os ,sys
import json

# acc_dic={
#     'id':1234,     #卡号
#     'password':'abc',  #密码
#     'credit':15000,       #信用额度
#     'balance':15000,     #余额度
#     'enroll_date':'2014-12-23',  #注册时间
#     'expir_date':'2019-12-22',  # 到期时间
#     'pay_day':22,
#     'status':0 ,  #0 正常  1 锁卡 2  遗失
#    "role":1
# }
acc_dic={
    'id':"admin",     #卡号
    'password':'abc123',  #密码
    'expir_date':'3000-12-22',#设置一个远大于今天的数值。管理员有效期
    'role':0      #0 管理员 1客户
}

# print(sys.platform) #返回操作系统平台名称
# print(sys.version) #获取Python解释程序的版本信息
def zhanghao(string):#生成一个测试用的银行G个人用户信息

    with open(r'account\%s.json'%acc_dic['id'],'w') as f:
        json.dump(string,f)


def main():
    if sys.platform=='win32':
        # print('这是Windows操作系统')
        if os.path.isdir('account'):#判断当前目录，是否存在文件名为‘account’的文件夹
            zhanghao(acc_dic)
        else:
            os.mkdir('account') # 如果文件夹不存在，则创建以一个新的文件夹
            zhanghao(acc_dic)
    else:
        print('本软件暂不兼容Windows以外的操作系统，如需帮助，请联系开发人员')

def del_file():#如果需要初始化数据，删除已有的数据文件，可以运行该程序
    print(os.listdir('account'))
    for i in os.listdir('account'):
        file=os.path.join('account',i)
        os.remove(file)

if __name__=='__main__':
    main()
    #del_file()