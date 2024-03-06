import sys

board = []

for i in range(10):
    add_board = list(sys.stdin.readline().strip())
    board.append(add_board)

def change(x,y):
    up = [x-1,y]
    down = [x+1,y]
    left = [x,y-1]
    right = [x,y+1]
    point = [x,y]
    points = [point, up, down, left, right]
    for p in points:
        if p[0] >=0 and p[0] <10 and p[1] >=0 and p[1] <10:
            if board[p[0]][p[1]] == "O":
                board[p[0]][p[1]] = "#"
            else:
                board[p[0]][p[1]] = "O"
ans = 0
def btn_click(s):
    global ans
    for i in range(1,10):
        for j in range(10):
            if board[i-1][j] == "O":
                change(i,j)
                print(*board,sep="\n")
                print()
                ans+=1

btn_click(0)
print(ans)
