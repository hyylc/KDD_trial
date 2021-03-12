from flask import Flask,jsonify,request,json
from datetime import datetime
from collections import Counter
import numpy as np
import random
import math
import re

from admin import Admin
from user import User
from setq import SetQ
from q import Q
from ans import Ans
from weight import Weight
from option import Option

"""
接口说明：
1.返回的是json数据
2.结构如下
{
    resCode:0 # 非0为错误
    data: #数据位置，一般为数组
    message: '对本次请求的说明'
}
"""

# 1.直接执行这个文件，那么__name__ = __main__
# 2.__name__ = 当前文件的名字

app = Flask(__name__) # 声明Flask类的变量
app.config['JSON_AS_ASCII'] = False

# 判断合法字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        # 说明合法
        return False
    else:
        # 不合法
        return True

# 转换日期格式/没用上
def getdate(dd):
    #dd = "Thu, 05 Nov 2020 23:25:45 GMT"
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.strptime(str(dd), GMT_FORMAT)

def MV(ans_list):
    """
    ans_list[i][j]: 问题i 用户j的回答
    """
    re = []
    for i in ans_list:
        collection_ans = Counter(i)
        re.append(collection_ans.most_common(1)[0][0])
    return re

def TD(user_list,q_list,ans_list):
    """
    ans_list[i][j]: 问题i 用户j的回答
    """
    ans_temp = []
    re = []
    weight = []
    for i in range(len(user_list)):
        weight.append(1.0/len(user_list))
    for i in range(len(q_list)):
        ans_temp.append(-1)

    while(1):
        # Answer Aggregation
        re = ans_temp
        ans_temp = []
        for i in ans_list:
            d = {}
            for item in range(len(i)):
                if i[item] not in d.keys():
                    d[i[item]] = weight[item]
                else:
                    d[i[item]] += weight[item]
            collection_d = Counter(d)
            ans_temp.append(collection_d.most_common(1)[0][0])
        print(ans_temp)

        # 和re[]比较，若答案收敛退出循环
        if re == ans_temp:
            print('回答收敛')
            break

        # Weight Estimation
        for i in range(len(user_list)):
            count = 0
            for j in range(len(ans_list)):
                if ans_list[j][i] == ans_temp[j]:
                    count = count + 1
            weight[i] = (count)*1.0/len(q_list)
        print(weight)

    return re,weight

#************用户接口************

# 用户注册（提供普通用户的注册功能）
# 用户信息（昵称，密码）
@app.route('/user_sign_up',methods=['POST','GET']) # 路由
def user_sign_up():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'name' : get_data['uname'],
            'pwd' : get_data['upwd']
        }
        #初始化
        u = User()
        data = u.sign_up(param)
        if data == False:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '注册失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '注册成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 用户登录（提供普通用户的注册功能）
# 用户信息（昵称，密码）
@app.route('/user_sign_in',methods=['POST','GET']) # 路由
def user_sign_in():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'name' : get_data['uname'],
            'pwd' : get_data['upwd']
        }
        #初始化
        u = User()
        data = u.sign_in(param)
        if data == None:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '登录失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '登录成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

#************管理员接口************
# 管理员注册
@app.route('/admin_sign_up',methods=['POST','GET']) # 路由
def admin_sign_up():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'name' : get_data['uname'],
            'pwd' : get_data['upwd']
        }
        #初始化
        a = Admin()
        data = a.sign_up(param)
        if data == False:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '注册失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '注册成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 管理员登录（提供管理员的注册功能）
# 管理员信息（昵称，密码）
@app.route('/admin_sign_in',methods=['POST','GET']) # 路由
def admin_sign_in():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'name' : get_data['uname'],
            'pwd' : get_data['upwd']
        }
        #初始化
        a = Admin()
        data = a.sign_in(param)
        if data == None:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '登录失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '登录成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

#************问题集合接口************
# 新建问题集合
@app.route('/new_setQ',methods=['POST','GET'])
def new_setQ():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'desc' : get_data['desc'],
            'pf' : get_data['pf'],
            'b' : get_data['b']
        }
        sq = SetQ()
        data = sq.new_setQ(param)
        if data == False:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '添加失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '已添加该问题'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 查看问题集合详情（涉及问题集合表，问题表，选项表）
@app.route('/setq_detail',methods=['POST','GET'])
def setq_detail():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'id_setq' : get_data['setq_id']
        }
        sq = SetQ()
        q = Q()
        sqdata = sq.setq_detail(param)
        qdata = q.allq(param)
        if sqdata == None:
            resData = {
                'resCode' : 1,
                'data' : [],
                'message' : '未查询到该问题集合'
            }
            return jsonify(resData)
        resData = {
            'resCode' : 0,
            'data' : [sqdata,qdata],
            'message' : '查询成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 查看所有问题集合
@app.route('/all_setq',methods=['POST','GET'])
def all_setq():
    if request.method == 'POST':
        # get_data = json.loads(request.get_data(as_text = True))
        sq = SetQ()
        data = sq.all_setq()
        resData = {
            'resCode' : 0,
            'data' : data,
            'message' : '查询成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


# 查看问题集合用户权重
@app.route('/weight_detail',methods=['POST','GET'])
def setq_weight_detail():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'setq_id' : get_data['setq_id']
        }
        w = Weight()
        data = w.allweight(param)
        if data == None:
            resData = {
                'resCode' : 1,
                'data' : [],
                'message' : '未查询到该问题集合的权重记录'
            }
            return jsonify(resData)
        resData = {
            'resCode' : 0,
            'data' : data,
            'message' : '查询成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

#************问题接口************
# 新建问题
@app.route('/new_Q',methods=['POST','GET'])
def new_Q():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'id_of_setq' : get_data['setq_id'],
            'desc' : get_data['desc'],
            'num' : get_data['num']
        }
        q = Q()
        data = q.new_Q(param)
        if data == False:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '添加失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '已添加该问题'            
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 查看问题详情（查询问题表，回答表，选项表）
@app.route('/q_detail',methods=['POST','GET'])
def q_detail():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'id_of_setq' : get_data['idq']
        }
        q = Q()
        a = Ans()
        qdata = q.q_detail(param)
        adata = a.allans(param)
        if qdata == None:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '查询失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,   
            "data" : [qdata,adata],
            "message" : '查询成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

#************选项接口************
@app.route('/new_Option',methods=['POST','GET'])
def new_Option():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'q_id' : get_data['q_id'],
            'desc' : get_data['desc'],
            # 这个num是选项在问题中的编号
            'num' : get_data['num']
        }
        o = Option()
        data = o.new_Option(param)
        if data == False:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '添加失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '已添加该选项'            
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

#************回答接口************
# 新建回答
@app.route('/new_Q',methods=['POST','GET'])
def new_Ans():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'user_id' : get_data['user_id'],
            'q_id' : get_data['q_id'], 
            'ans1' : get_data['ans1'],
            'ans2' : get_data['ans2']
        }
        a = Ans()
        data = a.new_ans(param)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : data,
                "message" : '回答已提交'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '提交失败'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


#************权重接口************
# 新纪录权重
@app.route('/new_weight',methods=['POST','GET'])
def new_weight():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'user_id' : get_data['u_id'],
            'setq_id' : get_data['q_id'], 
            'weight1' : get_data['w1'],
            'weight2' : get_data['w2']
        }
        w = Weight()
        data = w.new_weight(param)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : data,
                "message" : '权重已更新'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '更新失败'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


#************MV、TD方案接口************
# one-layer根据问题集合的扰动参数扰动
@app.route('/perturb_one',methods=['POST','GET'])
def perturb_one():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'id_setq' : get_data['setq_id'],
            'pf' : get_data['pf'],
            # 提交一份对所有问题的回答（qid 和 ans），并将所有回答按参数扰动
            'ans' : get_data['ans_list']
        }
        # param['ans'] = [[],[],[],[]]
        # 根据qid找到问题的回答数量s，按概率扰动
        for i in param['ans']:
            # i[0]  qid
            # i[1]  ans
            q = Q()
            param = {
                'id' : i[0]
            }
            data = q.q_detail(param)
            print('问题答案数量 ',data['q_num_of_ans'])
            s = data['q_num_of_ans']
            pro = np.random.uniform(0,1)
            print(pro)
            if pro <= param['pf']:
                i[1] = i[1]
            else:
                option = []
                for num in s:
                    if num != i[1]:
                        option.append(num)
                i[1] = random.sample(option,s-1)
            print(i[1])
        resData = {
            "resCode" : 0,
            "data" : param['ans'],
            "message" : '返回扰动结果'
        }
        return jsonify(resData)


# two-layer均匀选择扰动参数并按照扰动参数扰动
@app.route('/perturb_two',methods=['POST','GET'])
def perturb_two():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        param = {
            'id_setq' : get_data['setq_id'],
            'b' : get_data['b'],
            # 提交一份对所有问题的回答（qid 和 ans），并将所有回答按参数扰动
            'ans' : get_data['ans_list']
        }
        # param['ans'] = [[],[],[],[]]
        # 根据qid找到问题的回答数量s，按概率扰动
        pro = np.random.uniform(0,param['b'])
        for i in param['ans']:
            # i[0]  qid
            # i[1]  ans
            q = Q()
            param = {
                'id' : i[0]
            }
            data = q.q_detail(param)
            print('问题答案数量 ',data['q_num_of_ans'])
            s = data['q_num_of_ans']
            pro1 = np.random.uniform(0,pro)
            print(pro1)
            if pro1 <= pro:
                i[1] = i[1]
            else:
                option = []
                for num in s:
                    if num != i[1]:
                        option.append(num)
                i[1] = random.sample(option,s-1)
            print(i[1])
        resData = {
            "resCode" : 0,
            "data" : [pro, param['ans']],
            "message" : '返回扰动结果'
        }
        return jsonify(resData)


# 回答聚合
@app.route('/project_MV_and_TD',methods=['POST','GET'])
def project():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text = True))
        # 1.准备数据
        # 具体来说，获取数据库中所有该问题集合的问题，和所有用户的回答
        # q_list[]
        # ans1[]
        # ans2[]
        # ans1[i][j] 问题i 用户j
        # weight[i] 用户i的权重
        user_list = []
        q_list = []
        ans1 = []
        ans2 = []
        # 1.1找出所有问题id    
        param = {
            'id_setq' : get_data['setq_id']
        }     
        q = Q()
        data = q.allq_id(param)
        for i in data:
            q_list.append(i['idq'])
            ans1.append([])
            ans2.append([])
        # 1.2根据问题id确定回答问题的用户id
        # for i in range(len(q_list)):
        param = {
            'id_q' : q_list[0]
        }
        a = Ans()
        data = a.allans_userid(param)
        print(data)
        for item in data:
            if item['user_id'] not in user_list:
                user_list.append(item['user_id'])
        # 1.3对应问题id和用户id的所有回答，ans1和ans2
        for i in range(len(q_list)):
            for j in user_list:
                param = {
                    'id_q' : q_list[i],
                    'id_user' : j
                }
                a = Ans()
                data = a.allans_q_user(param)
                for item in data:
                    ans1[i].append(item['ans_one'])
                    ans2[i].append(item['ans_two']) 
        # 2.聚合结果
        # MV-one
        # MV-two
        q_MV_one = MV(ans1)
        for i in range(len(q_list)):
            param = {
                'id_q' : q_list[i],
                'ans' : q_MV_one[i]
            }
            q = Q()
            q.set_q_MV_one(param)
        q_MV_two = MV(ans2)
        for i in range(len(q_list)):
            param = {
                'id_q' : q_list[i],
                'ans' : q_MV_two[i]
            }
            q = Q()
            q.set_q_MV_two(param)
        # TD-one
        # TD-two
        # TD要返回对应的weight列表
        q_TD_one,weight_one = TD(user_list,q_list,ans1)
        for i in range(len(q_list)):
            param = {
                'id_q' : q_list[i],
                'ans' : q_TD_one[i]
            }
            q = Q()
            q.set_q_TD_one(param)
        q_TD_two,weight_two = TD(user_list,q_list,ans2)
        for i in range(len(q_list)):
            param = {
                'id_q' : q_list[i],
                'ans' : q_TD_two[i]
            }
            q = Q()
            q.set_q_TD_two(param)
        # 更新权重
        for i in range(len(user_list)):
            param = {
                'user_id' : user_list[i],
                'setq_id' : get_data['setq_id'],
                'weight1' : weight_one[i],
                'weight2' : weight_two[i]
            }
            w = Weight()
            w.new_weight(param)

#************用户接口************




#***********测试功能*********

if __name__ == '__main__': # 如果是直接执行文件，那么就执行下面的代码
    app.run(host = '127.0.0.1', port = 2021, debug = True)