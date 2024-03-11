import sys
input = sys.stdin.readline
tc = int(input())


def solve(start):
    global end
    q= []
    visit = [False for i in range(N+1)]
    ans =[]
    ans.append(icost[start])
    q.append(start)
    while q:
        now = q.pop(0)
        if now == end:
            break
        sub = dic[now]
        sub = sorted(sub, key=lambda x : -x[1])
        if sub:
            visit[sub[0][0]] = True
            q.append(sub[0][0])
            ans.append(sub[0])
    return ans

for _ in range(tc):
    N, K = map(int, input().split(" "))
    cost = [0] + list(map(int, input().split(" ")))
    index = [i for i in range(N+1)]
    icost = list(zip(index,cost))

    dic = {i : [] for i in range(1,N+1)}
    ans =1e9
    degree = [0 for i in range(N+1)]
    for i in range(K):
        a,b = map(int, input().split(" "))
        dic[a].append(icost[b])
        degree[b] +=1
    end = int(input())
    for i in range(1,N+1):
        if degree[i] == 0:
            temp = solve(i)
            ans = min(ans,sum([t[1] for t in temp]))
    print(ans)
