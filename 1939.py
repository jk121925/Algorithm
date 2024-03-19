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

def solve():
    global n,m
    s = 0
    e = 1000000000
    while s<=e:
        mid = (s+e)//2
        if bfs(mid):
            e = mid-1
        else:
            s = mid+1
    return s

def bfs(value):
    global n,m,start,end
    q = Queue()
    q.put((0,start))
    visit = [False for i in range(n+1)]
    visit[start] = True
    while not q.empty():
        now = q.get()
        if now[1] == end:
            return True
        for d in dic[now[1]]:
            if d[0] <= value:
                q.put(d)
                visit[d[1]] =True
            else:
                return False
    return False        

print(solve())
