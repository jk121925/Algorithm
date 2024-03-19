import sys
from queue import Queue
import heapq
input = sys.stdin.readline
INF = 1e10
n,m = map(int,input().split(" "))
dic = {i:[] for i in range(1,n+1)}

for i in range(m):
    a,b,c = map(int,input().split(" "))
    dic[a].append((c,b))
    dic[b].append((c,a))

start,end = map(int, input().split(" "))
def solve(start):
    global n,m
    dist = [0 for i in range(n+1)]
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        now = heapq.heappop(q)
        for d in dic[now[1]]:
            if dist[d[1]] < d[0] or dist[d[1]] < dist[now[1]]:
                dist[d[1]] = max(d[0],dist[now[0]])
                heapq.heappush(q,d)

    return dist
print(solve(start)[end])
