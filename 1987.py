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
    ans = max(ans,now)
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if nr >=0 and nr <R and nc >=0 and nc <C and not visit[ord(arr[nr][nc]) -ord('A')]: 
            visit[ord(arr[nr][nc])-ord('A')] = True
            dfs(nr,nc,now+1)
            visit[ord(arr[nr][nc])-ord('A')] = False

visit[ord(arr[0][0])-ord('A')] = True
dfs(0,0,0)
print(ans+1)
