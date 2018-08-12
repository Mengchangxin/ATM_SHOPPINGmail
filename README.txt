程序结构：
ATM
|——README
|——atm #ATM执行程序
|    |——__init__.py
|    |——bin#ATM执行程序目录
|    |    |——__init__.py
|    |    |——atm.py  #ATM执行程序
|    |    |——manage.py #ATM管理端，未实现
|    |——conf #配置文件
|    |    |——__init__.py
|    |    |——setting.py
|    |——core #主要程序逻辑 都在这个目录里
|    |    |——__init__.py
|    |    |——accounts.py #用于从文件里加载和存储账户数据
|    |    |——auth.py    #用户认证模块
|    |    |——db_handler.py #数据库连接引擎
|    |    |——logger.py     #日志记录模块
|    |    |——main.py     #主程序交互程序
|    |    |——transaction.py #记账、还钱、取钱等所有的与账户金额相关的操作
|    |——db   #用户数据存储的地方
|    |    |——__init__.py
|    |    |——account_sample.py #生成一个初始的账户数据，把这个数据存成一个 以这个账户id
|    |    |——account #存各个用户的账户数据，一个用户一个文件
|    |    |    |——1234.json #一个用户账户示例文件
|    |——log  #日志记录
|    |    |——__init__.py
|    |    |——access.log #用户访问和操作的相关日志
|    |    |——transactions.log  #所有的交易日志
|
|——shopping_mall  #电子商城程序，需要单独实现
|    |——__init__.py