import sys
import copy
input = sys.stdin.readline

n,a,b = map(int, input().split(" "))
city = []
q = []
for i in range(n):
    add_city = list(map(int,input().split(" ")))
    city.append(add_city)
    for j in range(n):
        q.append((i,j))


dx=[0,0,1,-1]
dy=[1,-1,0,0]



def check4(s):
    global a,b
    for i in range(4):
        x,y = s[0] +dx[i], s[1]+dy[i]
        if 0<=x<n and 0<=y<n and a<= abs(city[x][y] - city[s[0]][s[1]]) <=b:
            return True
    return False

def bfs(s,group):
    global n,a,b
    bfsq = []
    bfsq.append(s)
    num =1
    dic[group] +=city[s[0]][s[1]]
    while bfsq:
        now = bfsq.pop(0)
        visit[now[0]][now[1]] = group
        for i in range(4):
            x,y = now[0] + dx[i], now[1] +dy[i]
            if 0<=x<n and 0<=y<n and visit[x][y] ==-1:
                if a<= abs(city[now[0]][now[1]] - city[x][y])<=b:
                    visit[x][y] = group
                    bfsq.append((x,y))
                    dic[group] += city[x][y]
                    num+=1
    # print(dic[group])
    dic[group] //=num


def update():
    for i in range(n):
        for j in range(n):
            if visit[i][j]!=-1:
                city[i][j] = dic[visit[i][j]]

ans =0
while True:
    g = 0 
    flag=False
    innerqueue = copy.deepcopy(q)
    visit =[[-1 for i in range(n)] for i in range(n)]
    dic = {i:0 for i in range(n**2)}
    for qq in innerqueue:
        if visit[qq[0]][qq[1]] == -1 and check4(qq):
            bfs(qq,g)
            g+=1
    for idx in range(len(innerqueue)-1,-1,-1):
        target = q[idx]
        if visit[target[0]][target[1]] !=-1:
            flag = True
            city[target[0]][target[1]] = dic[visit[target[0]][target[1]]]
            innerqueue.remove(target)
    ans+=1
    for i in range(n):
        for j in range(n):
            if check4((i,j)):
                flag = True

    if flag:
        continue
    else:
        break
    
    
    
print(ans)
