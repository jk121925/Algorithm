import sys
from queue import Queue
input = sys.stdin.readline

n,m = map(int, input().split(" "))
board = [list(map(int,input().split(" "))) for i in range(n)]
island = []
for i in range(n):
    for j in range(m):
        if board[i][j] !=0:
            island.append((i,j))



dx =[0,0,1,-1]
dy =[1,-1,0,0]
def resolve(x,y):
    ret = 0
    for i in range(4):
        cx,cy = x +dx[i], y+dy[i]
        if 0<=cx<n and 0<=cy<m and board[cx][cy] == 0:
            ret+=1
    return ret

def dfs(s):
    inner_island = []
    inner_island.append(s)
    inner_q = Queue()
    inner_q.put(s)
    while not inner_q.empty():
        now = inner_q.get()
        for i in range(4):
            x,y = now[0] +dx[i], now[1] + dy[i]
            if 0<=x<n and 0<=y<m and (x,y) not in inner_island and board[x][y] !=0:
                inner_island.append((x,y))
                inner_q.put((x,y))
        # print(inner_island)
    return len(inner_island)
year =0
while True:
    flag = True
    if len(island) == 0:
        year = -1
        break
    if len(island) != dfs(island[0]):
        break
    erase = []
    for i in island:
        resolve_ret = resolve(i[0],i[1])
        if board[i[0]][i[1]] - resolve_ret <=0:
            erase.append(i)
        else:
            board[i[0]][i[1]] -=resolve_ret
    if len(erase) ==0:
        year = -1
        break

    for e in erase:
        board[e[0]][e[1]] = 0
        island.remove(e)
    year+=1
print(year)
