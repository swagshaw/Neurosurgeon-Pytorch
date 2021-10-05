'''
Descripttion: 
version: 
Author: Yang Xiao(YXIAO009@e.ntu.edu.sg)
Date: 2021-10-01 19:55:13
LastEditors: Yang Xiao
LastEditTime: 2021-10-01 19:56:46
'''
##假设有12道单项选择题，随机选择正确率是0.25，计算在能够确定某些题目的情况下的通过率
#####################
###假设全部随机选，7道以上正确为通过
#组合计算公式：c,m,n=n!/((n-m)!*m!)
def get_n(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1:
        return n*get_n(n-1)
count=0
for i in range(7,13):
    p=(get_n(12)/(get_n(12-i)*get_n(i)))*(0.25**i)*(0.75**(12-i))
    print('对{}题的概率是{}'.format(i,p))
    count=count+p
count
###############################################
###假设知道n题的答案（n<=7),其他随机选，成功率多少
#先假定an=3
for i in range(1,3):
    #知道多少题答案
    an=i
    #在知道多少题答案的情况下，计算得出大于60题的概率
    count=0
    for j in range(8-an,13-an):
        n=12-an
        p=(get_n(n)/(get_n(n-j)*get_n(j)))*(0.25**j)*(0.75**(n-j))
        #print(p)
        count=count+p
    print('在知道{}道题目的基础上随机蒙对大于等于7题的概率{}'.format(an,count))
