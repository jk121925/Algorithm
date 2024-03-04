import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

parent = [i for i in range(n)]

def getParent(a):
  if parent[a] == a:
    return a
  else:
    return getParent(parent[a])

def union(a,b):
  pa = getParent(a)
  pb = getParent(b)
  if pa > pb:
    parent[pa] = pb
  else:
    parent[pb] = pa

def check(a,b):
  if getParent(a) == getParent(b):
    return True
  else:
    return False
ans = -1
for i in range(m):
  a,b = map(int, input().split(" "))
  if check(a,b):
    if ans == -1:
      ans = i+1
  else:
    union(a,b)
print(ans) if ans != -1 else print(0)



