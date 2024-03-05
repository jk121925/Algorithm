import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000007
origin = [[1,1],[1,0]]

def x(o1,o2):
  ret = [[0,0],[0,0]]

  ret[0][0] = (o1[0][0] * o2[0][0] + o1[0][1] * o2[1][0]) % mod
  ret[0][1] = (o1[0][0] * o2[0][1] + o1[0][1] * o2[1][1]) % mod
  ret[1][0] = (o1[1][0] * o2[0][0] + o1[1][1] * o2[1][0]) % mod
  ret[1][1] = (o1[1][0] * o2[0][1] + o1[1][1] * o2[1][1]) % mod
  return ret

if n == 1 or n == 0:
  print(n)
else:
  n -=1
  A = [[1,0],[0,1]]
  while n>0:
    if n%2 == 1:
      A = x(A,origin)
    origin = x(origin,origin)
    n//=2
  print(A[0][0])



