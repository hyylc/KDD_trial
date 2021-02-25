from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Ans(object):
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

    
    # 插入一个回答
    def new_ans(self,param):
        sql = "select COUNT(*) from ans"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        id_count = self.cursor.fetchone()['COUNT(*)']
        sql = "insert into ans values (" + str(id_count+1) + "," + str(param['user_id']) + "," + str(param['q_id']) + "," + str(param['ans1']) + "," + str(param['ans2']) + ")"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 查询一个问题的所有回答
    def allans(self,param):
        sql = 'select * from ans where q_id = ' + str(param['id_q'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs
