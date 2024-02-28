import sys

n = int(sys.stdin.readline())
mod = 1000000007
dic = {i : [] for i in range(9)}

dic[0].append(1)
dic[0].append(2)
dic[1].append(0)
dic[1].append(3)
dic[1].append(2)
dic[2].append(0)
dic[2].append(1)
dic[2].append(3)
dic[2].append(4)
dic[3].append(1)
dic[3].append(2)
dic[3].append(4)
dic[3].append(6)
dic[3].append(5)
dic[4].append(3)
dic[4].append(2)
dic[4].append(6)
dic[5].append(3)
dic[5].append(6)
dic[5].append(7)
dic[6].append(4)
dic[6].append(3)
dic[6].append(5)
dic[6].append(8)
dic[7].append(5)
dic[7].append(8)
dic[8].append(7)
dic[8].append(6)


dp = [[0 for i in range(n+1)] for i in range(9)]
for d in dic[0]:
    dp[d][1] = 1
# print(*dp, sep="\n")
for i in range(2,n+1):
    for j in range(9):
        temp = 0
        for d in dic[j]:
            if dp[d][i-1] !=0:
                temp += dp[d][i-1] %mod
        dp[j][i] = temp % mod
# print()
print(dp[0][-1])
