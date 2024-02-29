import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int,input().split(" ")))
m = int(input())
b = list(map(int,input().split(" ")))

dic = defaultdict(int)
for i in range(n):
  for j in range(i,-1,-1):
    dic[sum(a[j:i+1])]+=1
# print(dic)
ans = 0
for i in range(m):
  for j in range(i,-1,-1):
    ans += dic[t-sum(b[j:i+1])]
print(ans)
