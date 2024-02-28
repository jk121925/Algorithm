import sys
input = sys.stdin.readline

n,m = map(int, input().split(" "))

degree = [0 for _ in range(n+1)]
dic = {i : [] for i in range(1,n+1)}

for _ in range(m):
    l = list(map(int, input().split(" ")))
    it = l[0]
    l = l[1:]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            dic[l[i]].append(l[j])
            degree[l[j]] +=1

q = []
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.pop(0)
    ans.append(now)
    for d in dic[now]:
        degree[d] -=1
        if degree[d] == 0:
            q.append(d)
print(*ans,sep="\n") if len(ans) == n else print(0)
