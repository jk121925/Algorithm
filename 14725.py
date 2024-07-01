import sys
from collections import OrderedDict
input = sys.stdin
n = int(input.readline())

dic = {}

def addDic(dic,treeDic):
    value = list(treeDic.keys())[0]
    if value in dic.keys():
        # print(value, dic, treeDic)
        # print(list(treeDic[value].keys()))
        dic[value][list(treeDic[value].keys())[0]]= treeDic[value][list(treeDic[value].keys())[0]]
        return
    else:
        return addDic(dic[value],treeDic[value])

def makeDic(dic,valueList,cnt):
    if cnt == len(valueList):
        return dic
    dic[valueList[cnt]] = {}
    makeDic(dic[valueList[cnt]],valueList,cnt+1)
    return dic

for i in range(n):
    splitInput = input.readline().split()
    treeDic = makeDic({},splitInput[1:],0)
    rootValue = splitInput[1]
    if rootValue not in list(dic.keys()):
        dic[rootValue] = treeDic[rootValue]
    else:
        addDic(dic,treeDic)
# print("dic",dic)

def dfs(dic,depth):
    keys = sorted(list(dic.keys()))
    for k in keys:
        print(k if depth==0 else "--" * depth + k)
        dfs(dic[k],depth+1)
    
dfs(dic,0)
