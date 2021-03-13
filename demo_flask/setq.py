from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class SetQ(object):
    def __init__(self): # 创建对象同时要执行的代码
        self.conn = connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'hyy19990907',
            database = 'kdd',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor(DictCursor) # 可以返回字典形式

    def __del__(self): # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()


    # 插入一个问题集合
    def new_setQ(self,param):
        sql = "select MAX(idsetq) from setq"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        rs = self.cursor.fetchone()
        if rs['MAX(idsetq)'] == None:
            id_count = 0
        else:
            id_count = rs['MAX(idsetq)']
        sql = "insert into setq values (" + str(id_count+1) + ",'" + str(param['desc']) + "'," + str(param['pf']) + "," + str(param['b']) + ")"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return str(id_count+1)
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 查询一个问题集合
    def setq_detail(self,param):
        # 查询问题集合表返回问题集合的描述和参数设置
        # （同时也要查询问题表）
        sql = "select * from setq where idsetQ = " + str(param['id_setq'])
        print(sql)
        self.cursor.execute(sql)
        rs = self.cursor.fetchone()
        return rs

    # 查询所有问题集合
    def all_setq(self):
        # 查询问题集合表返回问题集合的描述和参数设置
        # （同时也要查询问题表）
        sql = "select * from setq"
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs