import sys
input= sys.stdin.readline

n,m = map(int,input().split(" "))
board= [[1e9] *(n+1) for i in range(n+1)]
ans = [['-']*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split(" "))
    board[a][b]=c
    board[b][a]=c
    ans[a][b] =b
    ans[b][a] = a


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                ans[i][j] = ans[i][k]
            
for i in range(1,n+1):
    ans[i][i] = "-"
    ans[i] = ans[i][1:]
for l in ans[1:]:
    print(*l[1:],sep=' ')
