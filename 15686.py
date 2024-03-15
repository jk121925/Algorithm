import sys
input = sys.stdin.readline

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(index,num):
    global M,ret
    if num == M:
        local_sum =0
        for i in range(len(checken_house)):
            if alive[i]:
                local_sum += chichen_dist[i]
        ret = min(ret,local_sum)
        return 
    else:
        for i in range(index,len(checken_house)):
            if alive[i]:
                alive[i] = False
                solve(index+1,num-1)
                alive[i] = True
    return

N,M = map(int,input().split(" "))
board = []
checken_house = []
house = []
ret = 1e9
for i in range(N):
    board_add = list(map(int,input().split(" ")))
    board.append(board_add)
    for j in range(N):
        if board_add[j] == 2:
            checken_house.append((i,j))
        elif board_add[j] == 1:
            house.append((i,j))

alive = [True for _ in range(len(checken_house))]
chichen_dist = [0 for i in range(len(checken_house))]

for ch in range(len(checken_house)):
    dist_ = 0
    for h in house:
        dist_ += dist(h,checken_house[ch])
    chichen_dist[ch] = dist_
solve(0,len(checken_house))
print(ret)
