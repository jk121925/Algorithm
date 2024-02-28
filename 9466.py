import sys
input = sys.stdin

def dfs(x):
    global n
    visit = [False for _ in range(n+1)]
    s = [x]
    ret =[]
    while True:
        now = s.pop(-1)
        if visit[now]:
            break
        visit[now] = True
        ret.append(now)
        if x == parent[now]:
            return ret
        s.append(parent[now])

        

TC = int(input.readline())
for _ in range(TC):
    n = int(input.readline())
    parent =[0]+ list(map(int, input.readline().split(" ")))
    ans = n
    global_visit = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if not global_visit[i]:
            ret = dfs(i)
            if ret:
                print(ret)
                ans -=len(ret)
                for r in ret:
                    global_visit[r] = True
    print(ans)  
    
    


