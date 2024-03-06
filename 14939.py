import sys
import copy
board = []

for i in range(10):
    add_board = list(sys.stdin.readline().strip())
    board.append(add_board)

def change(x,y,sboard):
    up = [x-1,y]
    down = [x+1,y]
    left = [x,y-1]
    right = [x,y+1]
    point = [x,y]
    points = [point, up, down, left, right]
    for p in points:
        if p[0] >=0 and p[0] <10 and p[1] >=0 and p[1] <10:
            if sboard[p[0]][p[1]] == "O":
               sboard[p[0]][p[1]] = "#"
            else:
                
                sboard[p[0]][p[1]] = "O"
    return sboard
ans = 1e9

def btn_click(s):
    global ans
    sub_ans = 0
    sub_board = copy.deepcopy(board)

    for i in range(10):
        if s & (1<<i):
            sub_ans+=1
            sub_board = change(0,i,sub_board)
        
    for i in range(1,10):
        for j in range(10):
            if sub_board[i-1][j] == "O":
                sub_board = change(i,j,sub_board)
                sub_ans+=1
    if "O" not in sub_board[9]:
        ans = min(ans,sub_ans)

for i in range(1024):
    btn_click(i)

print(-1) if ans == 1e9 else print(ans)
