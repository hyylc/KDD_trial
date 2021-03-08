from flask import Flask,jsonify,request,json
from datetime import datetime
from collections import Counter
import numpy as np
import random
import re


user = [1,2,3,4]
q = [1,2,3,4]
a = [
    [2,2,3,5],
    [1,2,2,1],
    [1,1,1,3],
    [1,1,1,1]
]

def TD(user_list,q_list,ans_list):
    """
    ans_list[i][j]: 问题i 用户j的回答
    """
    ans_temp = []
    weight = []
    re = []
    for i in range(len(user_list)):
        weight.append(1.0/len(user_list))
    for i in range(len(q_list)):
        ans_temp.append(-1)
    print('初始权重 ',weight)
    
    while(1):
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
            print(d)
            ans_temp.append(collection_d.most_common(1)[0][0])
        
        print('聚合的回答 ',ans_temp)

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
        print('更新后的权重 ',weight)


TD(user,q,a)