#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author:Administrator
#date:2018/7/14

#参数配置文件
import os,sys,logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#/Atm

DATABASE = {
    'engine': 'file_storage',
    'name': 'account',
    'path': "%s/db" % BASE_DIR#../Atm
}

LOG_LEVEL = logging.INFO  #记录等级
LOG_TYPES = {
    'transaction': 'transaction.log',
    'access': 'access.log'
}

#发生交易的配置类型
TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},#还款
    'withdraw':{'action':'minus','interest':0.05},#取现是降低可用余额
    'transfer':{'action':'minus','interest':0.05},#转账是降低可用余额
    'consume':{'action':'minus','interest':0},
}