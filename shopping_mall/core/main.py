#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Administrator 
2018/8/14 
'''
import os,sys,logging,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import accounts
from core import logger
shopping_log=logger.logger("shopping")

product_list=accounts.load_current_balance()
#print(product_list)


def shopping_action(sum_amount):
        # saving=input("please input your saving:")
        saving=sum_amount
        shopping_car=[]
        if saving.isdigit():
                saving=float(saving)
                while True:
                        for j in product_list.items():
                                print(j)
                        choice=input('choice your product number[quit:q]')
                        if choice.isdigit():
                                if choice in product_list:
                                        p_item=product_list[choice]
                                        for name,price in p_item.items():
                                                continue
                                        if price<saving:
                                                saving-=price
                                                shopping_car.append(p_item)
                                                shopping_log.info("选购商品 {name}  价格是：{price}".format(name=name,price=price))#记录购物信息
                                        else:
                                                print('余额不足，还剩%s'%saving)
                                        print(p_item)
                                else:
                                        print('number is out inside')
                        elif choice.lower()=='q':
                                print('----------已经购买如下商品-------------')
                                print('编码','商品名称','商品价格','数量',sep='\t')
                                y_sum=[]
                                x = 1
                                for y in shopping_car:

                                        if y not in y_sum:
                                                for y_1,y_2 in y.items():
                                                        continue
                                                print(x,y_1,y_2,shopping_car.count(y),sep='\t')
                                                y_sum.append(y)
                                                time.sleep(1)
                                                x=x+1

                                #print('剩余金额%s'%saving)
                                cost_cash=float(sum_amount)-saving  # 返回消费的金额
                                return cost_cash
                                break
                        else:
                                print("invalid input")

if __name__=="__main__":
        shopping_action("50000")