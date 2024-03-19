import sys
import bisect 
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split(" ")))
kv = list(zip(range(1,n+1),l))

ans =[]
for i in range(len(kv)):
    if len(ans) == 0:
        ans.append(kv[i][1])
        continue
    if ans[-1] > kv[i][1]:
        ans[bisect.bisect_left(ans,kv[i][1])] = kv[i][1]
    else:
        ans.append(kv[i][1])
print(len(ans))
