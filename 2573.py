import sys
from queue import Queue
# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

input = sys.stdin.readline

n,m = map(int,input().split(" "))
board = [list(map(int,input().split(" "))) for i in range(n)]

q= []
for i in range(n):
    for j in range(m):
        if board[i][j] !=0:
            q.append((i,j))

q.sort()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def resolve(x,y):
    ret = 0
    for i in range(4):
        cx,cy = x +dx[i], y+dy[i]
        if 0<=cx<n and 0<=cy<m and board[cx][cy] == 0:
            ret+=1
    return ret

def bfs(s):
    local_q = Queue()
    local_q.put(s)
    ret = 1
    visit[s[0]][s[1]] = True
    while not local_q.empty():
        now = local_q.get()
        for i in range(4):
            x,y = now[0] +dx[i], now[1] +dy[i]
            if 0<=x<n and 0<=y<m and not visit[x][y] and board[x][y] !=0:
                visit[x][y] = True
                ret+=1
                local_q.put((x,y))
    return ret
year =1

while True:
    flag = True
    visit = [[False for i in range(m)] for i in range(n)]
    for qq in q:
        if board[qq[0]][qq[1]] !=0 and visit[qq[0]][qq[1]] == 0:
            temp_ = bfs((qq[0],qq[1]))
            if temp_ < len(q):
                flag = False
                break

    if not flag:
        break
            # group+=1
    # for i in range(n):
    #     for j in range(m):
    #         if board[i][j] !=0 and visit[i][j] == 0:
    #             bfs((i,j))
    #             group+=1
    q.sort()
    eraseq = []
    for i in range(len(q)-1,-1,-1):
        rx,ry = q[i][0],q[i][1]
        ch = resolve(rx,ry)
        if board[rx][ry] -ch <=0:
            eraseq.append((rx,ry))
        else:
            board[rx][ry] -=ch
    for ex,ey in eraseq:
        board[ex][ey] = 0
        q.remove((ex,ey))
        
    # print(*board,sep="\n")
    # print()
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                flag = False


    temp_sum =0 
    for i in range(n):
        temp_sum += sum(board[i])
    if temp_sum == 0:
        flag = True
        break

    if len(q) == n**2:
        flag = True
        break
            
    year+=1
if flag:
    print(-1)
else:
    print(year)
