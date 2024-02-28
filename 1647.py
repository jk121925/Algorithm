import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split(" "))

dic = {i : [] for i in range(1,n+1)}
sumcost = 0
for _ in range(m):
    a,b,c = map(int,input().split(" "))
    dic[a].append((c,b))
    dic[b].append((c,a))

q = []
edge = []
visit = [False for _ in range(n+1)]
heapq.heappush(q,(0,1))
for _ in range(n):
    while True:
        if visit[q[0][1]] == False:
            break
        else:
            heapq.heappop(q)
    now = heapq.heappop(q)
    visit[now[1]] = True
    edge.append(now)
    sumcost += now[0]
    for d in dic[now[1]]:
        if not visit[d[1]]:
            heapq.heappush(q,d)    
    # print(now,q,visit)
# print(max(list(map(lambda x : x[0],edge))))
# while q:
#     print(q,visit)
#     now = heapq.heappop(q)
#     print(now)
#     edge.append(now)
#     sumcost -=now[0]
#     visit[now[1]] = True
#     for d in dic[now[1]]:
#         if not visit[d[1]]:
#             heapq.heappush(q,d)
print(sumcost - max(list(map(lambda x : x[0],edge))))
