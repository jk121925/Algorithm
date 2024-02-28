import sys
input = sys.stdin

def dfs(x):
    global ans
    visit.append(x)
    print(visit)
    global_visit[x] = True
    next = parent[x]
    if global_visit[next]:
        if next in visit:
            ans -= len(visit[visit.index(next):])
            return
    else:
        dfs(next)

        

TC = int(input.readline())
for _ in range(TC):
    n = int(input.readline())
    parent =[0]+ list(map(int, input.readline().split(" ")))
    ans = n
    global_visit = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if not global_visit[i]:
            visit = []
            dfs(i)
    print(ans)   
    
    


