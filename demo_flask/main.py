from flask import Flask,jsonify,request,json
from datetime import datetime
import re

from admin import Admin
from user import User

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



#***************接口函数********************
# 用户注册（提供普通用户的注册功能）
# 用户信息（昵称，密码）
@app.route('/user_sign_up',methods=['POST']) # 路由
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
@app.route('/user_sign_in',methods=['POST']) # 路由
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





















#***********测试功能*********


if __name__ == '__main__': # 如果是直接执行文件，那么就执行下面的代码
    app.run(host = '127.0.0.1', port = 2021, debug = True)