import sys
import heapq
input = sys.stdin

V,E = map(int, input.readline().split(" "))

dic = {}

for i in range(1,V+1):
    dic[i] = []

start = 0
for i in range(E):
    a,b,c = map(int, input.readline().split(" "))
    if start == 0:
        start = a
    dic[a].append((c,b))
    dic[b].append((c,a))

def spanningTree(start):
    global V
    ans =0
    count =0
    arr =[]
    visit = [False for _ in range(V+1)]
    heapq.heappush(arr,(0,start))

    while arr:
        now = heapq.heappop(arr)
        if  visit[now[1]]:
            continue
        ans += now[0]
        count+=1
        visit[now[1]] = True
        if count == V:
            break
        for e in dic[now[1]]:
            heapq.heappush(arr,e)

    return ans

print(spanningTree(start))
