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


def bfs(value):
    global n,m,start,end
    q = Queue()
    q.put(start)
    visit = [False for i in range(n+1)]
    visit[start] = True
    while not q.empty():
        now = q.get()
        for cost,next in dic[now]:
            if not visit[next] and cost >= value:
                q.put(next)
                visit[next] =True
    if visit[end]:
        return True
    else:
        return False        

s = 1
e = 1000000000
ret = 0
while s<=e:
    mid = (s+e)//2
    if bfs(mid):
        ret = mid
        s = mid+1
    else:
        e = mid-1
print(ret)
