import sys

input = sys.stdin

R, C= map(int, input.readline().split(" "))

arr = []
for _ in range(R):
    addarr = list(input.readline().strip())
    arr.append(addarr)

visit = [False for _ in range(26)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans =0
def dfs(r,c,now):
    global R,C
    global ans
    if visit[ord(arr[r][c])-65] == True:
        ans = max(ans,now)
        return
    else:
        visit[ord(arr[r][c])-65] = True
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if nr >=0 and nr <R and nc >=0 and nc <C: 
                dfs(nr,nc,now+1)
        visit[ord(arr[r][c])-65] = False


dfs(0,0,0)
print(ans)
