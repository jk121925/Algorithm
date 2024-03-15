import sys
input = sys.stdin.readline

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(index,num):
    global M,ret
    if num == len(checken_house)-M:
        local_sum =0 
        for i in range(len(house)):
            local_sum += min(num for cond, num in zip(alive,dp[i]) if cond)
        ret = min(ret,local_sum)
        return 
    else:
        for i in range(index,len(checken_house)):
            if alive[i]:
                alive[i] = False
                solve(i+1,num+1)
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
dp = [[0 for _ in range(len(checken_house))] for _ in range(len(house))]

for j in range(len(house)):
    for i in range(len(checken_house)):
        dp[j][i] = dist(checken_house[i],house[j])

solve(0,0)
print(ret)
