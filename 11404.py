# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

import sys
input = sys.stdin

v = int(input.readline())
e = int(input.readline())
 
graph = [[0 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a,b,w  = map(int,input.readline().split(" "))
    if graph[a][b]!=0:
        if graph[a][b] > w:
            graph[a][b] = w
    else:
        graph[a][b] =w

dist = [[1e9 for _ in range(v)] for _ in range(v)]
for i in range(v):
    for j in range(v):
        if graph[i+1][j+1] !=0:
            dist[i][j] = graph[i+1][j+1]
        if i == j:
            dist[i][j] =0

for k in range(v):
    for i in range(v):
        for j in range(v):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans =""
for d in dist:
    for di in d:
        if di == 1e9:
            ans += str(0) + " "
        else:
            ans += str(di) + " "
    ans.strip()
    ans += "\n"
print(ans.strip())
