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

for d in dist:
    print(*d, sep=" ")
