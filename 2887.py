import sys
import heapq
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
def getParent(a):
  if a == parent[a]:
    return a
  return getParent(parent[a])

def union(a,b):
  pa = getParent(a)
  pb = getParent(b)
  if pa < pb:
    parent[pb] = pa
  else:
    parent[pa] = pb

def isloog(a,b):
  if getParent(a) == getParent(b):
    return True
  return False

X = []
Y = []
Z = []
edge = []
for i in range(n):
  x,y,z = map(int, input().split(" "))
  X.append((x,i))
  Y.append((y,i))
  Z.append((z,i))

X.sort()
Y.sort()
Z.sort()

for i in range(n-1):
  edge.append((X[i+1][0]-X[i][0],X[i][1],X[i+1][1]))
  edge.append((Y[i+1][0]-Y[i][0],Y[i][1],Y[i+1][1]))
  edge.append((Z[i+1][0]-Z[i][0],Z[i][1],Z[i+1][1]))

edge.sort()
ans =0
for i in range(len(edge)):
  c,s,e = edge[i][0],edge[i][1],edge[i][2]
  if isloog(s,e):
    continue
  else:
    union(s,e)
    ans +=c


print(ans)


