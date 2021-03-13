from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回
from option import Option

class Q(object):
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
   
    # 插入一个问题
    def new_Q(self,param):
        sql = "select MAX(q.idq) from q"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        # print('max(q.idq) = ',self.cursor.fetchone()['MAX(q.idq)'])
        rs = self.cursor.fetchone()
        if rs['MAX(q.idq)'] == None:
            id_count = 0
        else:       
            id_count = rs['MAX(q.idq)']
        print(id_count)
        sql = "insert into q (idq,q_id_of_setq,q_description,q_num_of_ans) values (" + str(id_count+1) + "," + str(param['id_of_setq']) + ",'" + param['desc'] + "'," + str(param['num']) + ")"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return str(id_count+1)
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False


    # 查询一个问题
    def q_detail(self,param):
        # 查询问题表返回问题的描述
        sql = "select * from q where idq = " + str(param['id'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchone()
        return rs

    # 返回问题集合的所有问题
    def allq(self,param):
        sql = 'select * from q where q_id_of_setq = ' + str(param['id_setq'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        # 接下来根据所有问题的idq查询每个问题的所有选项，一起返回
        ans_list = []
        for i in rs:
            p = {
                'id_q' : i['idq']
            }
            o = Option()
            data = o.alloption(p)
            print(data)
            ans_list.append(data)
        return rs,ans_list

    # 返回问题集合的所有问题id
    def allq_id(self,param):
        sql = 'select idq from q where q_id_of_setq = ' + str(param['id_setq']) + ' order by idq ASC'
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs

    # 将聚合的回答保存到数据库中（考虑后续会更新的问题）
    def set_q_MV_one(self,param):
        sql = 'select idq from q where q_id_of_setq = ' + str(param['id_setq'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs

    def set_q_MV_two(self,param):
        sql = 'update q set q_MV_two = ' + str(param['ans']) + ' where q_id_of_setq = ' + str(param['id_setq'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs
    
    def set_q_TD_one(self,param):
        sql = 'select idq from q where q_id_of_setq = ' + str(param['id_setq'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs

    def set_q_TD_two(self,param):
        sql = 'select idq from q where q_id_of_setq = ' + str(param['id_setq'])
        self.cursor.execute(sql)
        rs = self.cursor.fetchall()
        return rs
        