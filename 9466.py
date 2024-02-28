import sys
input = sys.stdin

def dfs(x):
    global ans
    s = [x]
    visit.append(x)
    global_visit[x] = True
    while s:
        now = s.pop(-1)
        next = parent[now]
        if global_visit[next]:
            if next in visit:
                ans -= len(visit[visit.index(next):])
                return
        else:
            visit.append(next)
            global_visit[next]  = True
            s.append(next)

        

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


