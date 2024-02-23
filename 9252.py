# ACAYKP
# CAPCAK

import sys
input = sys.stdin

s1 = input.readline().strip()
s2 = input.readline().strip()


dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# maxcnt =1e9
# anscnt =1e9
# ansstr = ""
# for i in range(len(s2)-1,-1,-1):
#     for j in range(len(s1)-1,-1,-1):
#         if s2[i] == s1[j] and maxcnt > dp[i][j]:
#             maxcnt = dp[i][j]
#             ansstr = s2[i] +ansstr
#             if anscnt == 1e9:
#                 anscnt = dp[i][j]
#             break
print(*dp,sep="\n")

# print(anscnt)
# print(ansstr)
