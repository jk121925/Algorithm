import sys
input = sys.stdin.readline

def getParent(x):
    if x == parent[x]:
        return x
    else:
        return getParent(parent[x])

def union(a,b):
    pa = getParent(a)
    pb = getParent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def isSet(a,b):
    pa = getParent(a)
    pb = getParent(b)
    if pa == pb:
        return True
    else:
        return False
n,m = map(int,input().split(" "))
parent = [i for i in range(n+1)]
for _ in range(m):
    p,a,b = map(int, input().split(" "))
    if p == 1:
        if isSet(a,b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)
