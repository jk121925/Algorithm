
import sys
input = sys.stdin.readline
tc = int(input())


def solve():
    global N
    q= []
    sumcost = [0 for i in range(N+1)]
    visit = [False for i in range(N+1)]
    for i in range(1,N+1):
        if degree[i] == 0:
            sumcost[i] = cost[i]
            visit[i] = True
            q.append(i)
    # print(sumcost)
    while q:
        now = q.pop(0)
        for d in dic[now]:
            degree[d] -= 1
            sumcost[d] = max(sumcost[d] ,sumcost[now] + cost[d])
            if degree[d] == 0:
                q.append(d)
                visit[d] = True
        # print(sumcost)
    return sumcost

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
        dic[a].append(b)
        degree[b] +=1
    end = int(input())
    temp = solve()
    print(temp[end])
