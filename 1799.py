import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
  boardadd = list(map(int, input().split(" ")))
  board.append(boardadd)

white = []
black = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      if  (i+j) %2 == 0:
        white.append((i,j))
      else:
        black.append((i,j))

    

# print(one)
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
def check(a):
  global n
  flag =True
  for i in range(4):
    next = a
    while flag:
      if next[0] >=0 and next[0]<n and next[1] >=0 and next[1] <n:
        if board[next[0]][next[1]] == 2:
          flag = False
        next = (next[0]+dx[i], next[1]+dy[i])
      else:
        break
    if flag == False:
      return False
  return True





def dfs(pointer,one):
  global n, ans, temp
  ans = max(ans, temp)
  for i in range(pointer, len(one)):
    o = one[i]
    if check(o):
      board[o[0]][o[1]] = 2
      temp +=1
      dfs(i,one)
      temp -=1
      board[o[0]][o[1]] = 1

if n == 1:
  if board[0][0] == 1:
    print(1)
  else:
    print(0)
else:
  ans = 0
  temp = 0
  a =0
  dfs(0,white)
  a+=ans
  ans =0
  temp =0
  dfs(0,black)
  a+=ans
  print(a)
