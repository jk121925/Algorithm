import sys

n = int(sys.stdin.readline())
mod = 1000000007

v = [
    [0,1,1,0,0,0,0,0],
    [1,0,1,1,0,0,0,0],
    [1,1,0,1,1,0,0,0],
    [0,1,1,0,1,1,0,0],
    [0,0,1,1,0,1,0,1],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,1,0,1,0,]
]

def multiple(v1,v2):
    retans = [[0 for i in range(8)] for _ in range(8)]
    for i in range(len(v1)):
        for j in range(len(v2)):
            for k in range(8):
                retans[i][j] += v1[i][k] * v2[k][j]
                retans[i][j] %= mod
            retans[i][j] %= mod
    return retans
    # return[[sum(v1[i][k] * v2[k][j] % mod for k in range(8)) % mod for j in range(8)] for i in range(8)]

ans =[[0] * 8 for _ in range(8)]
for i in range(8):
    ans[i][i] = 1
while n >0:
    if n%2 != 0:
        ans = multiple(ans,v)
        n  -= 1
    v = multiple(v,v)
    n//=2
print(ans[0][0])
