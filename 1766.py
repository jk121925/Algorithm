import sys
import heapq
input = sys.stdin

n,m = map(int, input.readline().split(" "))

degree = [0 for _ in range(n+1)]
dic = {i:[] for i in range(n+1)}

for _ in range(m):
    a,b = map(int, input.readline().split(" "))
    dic[a].append(b)
    degree[b] +=1

arr=[]
visit = [False for _ in range(n+1)]
for i in range(1,n+1):
    if degree[i] == 0:
        heapq.heappush(arr,i)
ans = []

while arr:
    now = heapq.heappop(arr)
    for d in dic[now]:
        degree[d] -=1
        if degree[d] ==0:
            heapq.heappush(arr,d)
    ans.append(now)

print(*ans, sep=" ")
