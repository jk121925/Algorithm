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
    while True:
        if visit[i] == 1:
            if i == x:
                return True  
            else:
                break
        visit[i] =1
        i = parent[i]
        
    return False
    

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
    for i in range(1,len(parent)):
        if not travel(i):
            ans +=1
    print(ans)
