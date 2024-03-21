mport sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split(" "))

dic = {i:[] for i in range(N+1)}

for _ in range(M):
    a,b,c = map(int, input().split(" "))
    dic[a].append((c,b))
    dic[b].append((c,a))

ans =[]

dist = [[1e9,-1] for i in range(N+1)]

q = []
q.append((0,1))
dist[1][1] = 0
dist[1][0] = 1
while q:
    now = heapq.heappop(q)
    for d in dic[now[1]]:
        if dist[d[1]][0] > dist[now[1]][0] + d[0]:
            dist[d[1]][0] = dist[now[1]][0] +d[0]
            dist[d[1]][1] = now[1]
            q.append(d)
ans = []
for i in range(2,N+1):
    ans.append(str(i) +" "+ str(dist[i][1]))
print(len(ans))
print(*ans,sep="\n")


