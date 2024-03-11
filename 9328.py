import sys
import copy
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solve(queue):
    global key,R,C
    ans = 0
    visit = [[False for i in range(C)] for i in range(R)]
    innerqueue = copy.deepcopy(queue)
    stage = []
    for q in innerqueue:
        if q[0] in key or q[0] == '.':
            stage.append(q)
    while stage:
        now = stage.pop(0)
        visit[now[1]][now[2]] = True
        for i in range(4):
            nextx, nexty = now[1] +dx[i], now[2] +dy[i]
            if nextx >=0 and nextx <R and nexty >=0 and nexty <C and not visit[nextx][nexty]:
                point = board[nextx][nexty]
                visit[nextx][nexty] = True
                if point == '#':
                    continue
                elif point == '.':
                    stage.append(('.',nextx,nexty))
                elif point == '$':
                    stage.append(('$',nextx,nexty))
                    ans +=1
                elif point.isalpha():
                    if point.islower():
                        if point not in key:
                            key.append(point)
                            stage.append((point,nextx,nexty))
                            for q in range(len(innerqueue)-1,-1,-1):
                                if innerqueue[q][0].lower() in key:
                                    stage.append(innerqueue.pop(q))
                        else:
                            stage.append((point,nextx,nexty))
                    elif point.isupper():
                        if point.lower() in key:
                            stage.append((point,nextx,nexty))
                        else:
                            innerqueue.append((point,nextx,nexty))
    return ans


tc = int(input())
for _ in range(tc):
    R,C = map(int, input().split(" "))
    board = []
    starting = []
    target = 0
    for r in range(R):
        board_add = list(input().strip())
        target += list(map(lambda x : x == '$',board_add)).count(True)
        if r == 0 or r == R-1:
            for c in range(C):
                if board_add[c] != '*':
                    starting.append((board_add[c],r,c))
        else:
            if board_add[0] != '*':
                starting.append((board_add[0],r,0))
            if board_add[C-1] != '*':
                starting.append((board_add[C-1],r,C-1))
        board.append(board_add)
    key = list(input().strip())
    print(solve(starting))
