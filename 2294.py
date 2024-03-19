import sys
input = sys.stdin.readline

n,k = map(int,input().split(" "))
l = [int(input()) for i in range(n)]
l.sort()


dp = [[1e9 for i in range(k+1)] for i in range(k+1)]
for c in l:
    dp[1][c] = 1
flag = False
for i in range(2,k+1):
    for j in range(k+1):
        for c in l:
            if j-c>0:
                dp[i][j] = min(dp[i][j],dp[i-1][j-c]+1)
                if j == k and dp[i][j]!=1e9:
                    flag = True
    if flag:
        print(dp[i][k])
        break
if not flag:
    print(-1)
