import sys
input = sys.stdin.readline

n,k = map(int,input().split(" "))
l = [int(input()) for i in range(n)]
l.sort()


dp = [[10000000 for i in range(k+1)] for i in range(k+1)]
for c in l:
    dp[1][c] = 1
for i in range(2,k+1):
    for j in range(k+1):
        for c in l:
            if j-c>0:
                dp[i][j] = min(dp[i][j],dp[i-1][j-c]+1)

ans = 1e9
for i in range(k+1):
    ans = min(dp[i][k],ans)
print(-1 if ans == 1e9 else ans)
