from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Admin(object):
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
    
    #管理员注册
    def sign_up(self,item):
        sql = "select COUNT(*) from admin"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        id_count = self.cursor.fetchone()['COUNT(*)']
        sql = "insert into admin values (" + str(id_count+1) + ",'" + item['name'] + "','" + item['pwd'] + "')"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    #查询用户名是否已存在


    #登录处理（查询用户名和密码是否存在）
    def sign_in(self,item):
        # 查找管理员表
        sql = "select * from admin where admin_name = %s and admin_password = %s"
        self.cursor.execute(sql,[item['name'],item['pwd']])
        # 处理结果，查询单条数据，无需提交
        rs = self.cursor.fetchone()
        return rs

