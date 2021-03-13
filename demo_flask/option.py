from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Option(object):
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
   
    # 插入一个选项
    def new_Option(self,param):
        sql = "select MAX(idoption) from op"
        id_count = 0
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        rs = self.cursor.fetchone()
        if rs['MAX(idoption)'] == None:
            id_count = 0
        else:       
            id_count = rs['MAX(idoption)']   
        print(id_count)    
        sql = "insert into op (idoption,q_id,option_description,option_num) values (" + str(id_count+1) + "," + str(param['q_id']) + ",'" + param['desc'] + "'," + str(param['num']) + ")"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False


    # 返回问题的所有选项
    def alloption(self,param):
        sql = 'select * from op where q_id = ' + str(param['id_q']) + ' order by option_num ASC'
        print(sql)
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs

        