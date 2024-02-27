import sys
input = sys.stdin
def getParent(x):
    if x == parent[x]:
        return x
    else:
        return getParent(parent[x])
def travel(x):
    global n
    visit = [0 for _ in range(n+1)]
    visit[x] = 1
    i = parent[x]
    ret = [x]
    while True:
        if visit[i] == 1:
            if i == x:
                return ret 
            else:
                break
        visit[i] =1
        ret.append(i)
        i = parent[i]
        
    return []
    

def union(a,b):
    # pa = getParent(a)
    # pb = getParent(b)
    parent[a] = b

TC = int(input.readline())
for _ in range(TC):
    n = int(input.readline())
    parent = [i for i in range(n+1)]
    l = list(map(int, input.readline().split(" ")))
    ans = 0
    for index, vector in enumerate(l):
        union(index+1,vector)
    global_visit = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        if global_visit[i] == 0:
            ret_list = travel(i)
            if ret_list:
                ans +=len(ret_list)
                for r in ret_list:
                    global_visit[r] = 1
    print(n-ans)
