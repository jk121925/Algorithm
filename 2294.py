import sys
input = sys.stdin.readline

n,k = map(int,input().split(" "))
l = [int(input()) for i in range(n)]
l.sort()


dp = [1e9 for i in range(k+1)]
dp[0]=0
for c in l:
    dp[c] = 1
for i in range(2,k+1):
    m = 1e9
    for c in l:
        if i-c>0:
            m = min(dp[i-c]+1,min(dp[i],m)) 
    dp[i] = m
print(dp[-1])
