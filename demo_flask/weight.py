from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Weight(object):
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
   
    # 插入一个权重
    # 在管理员每次使用TD的时候，最后更新weight （若有旧数据，就更新，没有就插入新的）
    def new_weight(self,param):
        sql = "select * from weight where user_id = " + str(param['user_id']) + " and setq_id = " + str(param['setq_id'])
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
        except:  
            self.conn.rollback()                   # Rollback in case there is any error
        rs = self.cursor.fetchone()
        num1 = "{:.5f}".format(param['weight1'])
        num2 = "{:.5f}".format(param['weight2'])
        print('num1 = ',num1,'  num2 = ',num2)
        if rs != None:
            sql = "update weight set weight_one = " + str(num1) + ", weight_two = " + str(num2) + " where user_id = " + str(param['user_id']) + " and setq_id = " + str(param['setq_id'])
            print(sql)
            try:
                self.cursor.execute(sql)             # 执行单条sql语句
                self.conn.commit()                     # 提交到数据库执行
                return True
            except:
                self.conn.rollback()                   # Rollback in case there is any error
                return False
        else:
            sql = "select MAX(idweight) from weight"
            try:
                self.cursor.execute(sql)             # 执行单条sql语句
                self.conn.commit()                     # 提交到数据库执行
            except:
                self.conn.rollback()                   # Rollback in case there is any error
            rs = self.cursor.fetchone()
            if rs['MAX(idweight)'] == None:
                id_count = 0
            else:       
                id_count = rs['MAX(idweight)']
            print(id_count)
            sql = "insert into weight values (" + str(id_count+1) + "," + str(param['user_id']) + ","+ str(param['setq_id']) + ","+ str(num1) + "," + str(num2) + ")"
            print(sql)
            try:
                self.cursor.execute(sql)             # 执行单条sql语句
                self.conn.commit()                     # 提交到数据库执行
                return True
            except:
                self.conn.rollback()                   # Rollback in case there is any error
                return False

    # 查询一个问题集合中所有用户的权重
    def allweight(self,param):
        sql = 'select user_id,weight from weight where setq_id = ' + str(param['setq_id'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs
    