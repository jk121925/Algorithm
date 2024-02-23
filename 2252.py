import sys
input = sys.stdin

def dfs(s, value):
    if len(dic[s]) == 0:
        ans.append(value + cost[s])
        return value + cost[s]
    for e in dic[s]:
        dfs(e,value + cost[s])
                

TC = int(input.readline())
for _ in range(TC):
    n,m = map(int,input.readline().split(" "))
    cost = [0] +list(map(int, input.readline().split(" ")))
    dic = {i: [] for i in range(1,n+1)}
    degree = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input.readline().split(" "))
        dic[b].append(a)
        # degree[b] +=1
    target = int(input.readline())
    for i in range(1,n+1):
        for e in dic[i]:
            if e != target:
                degree[e] +=1
    q = []
    print(degree)
    print(dic)
    q.append(target)
    ans =[]
    ret= 0
    dfs(target,0)
    print(ans)
