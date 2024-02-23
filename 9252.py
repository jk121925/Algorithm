# ACAYKP
# CAPCAK

import sys
input = sys.stdin

s1 = input.readline().strip()
s2 = input.readline().strip()


dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
retans = 0
for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
            retans = max(dp[i][j],retans)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            

retstr = ""

s1p=len(s1)
s2p=len(s2)

while s1p >0 and s2p >0:
    if dp[s2p][s1p] ==dp[s2p][s1p-1]:
      s1p-=1
    # 이줄 때문에
    elif dp[s2p][s1p] == dp[s2p-1][s1p]:
      s2p-=1
    else:
        retstr =  s1[s1p-1] + retstr
        s1p-=1
        s2p-=1

# print(*dp, sep="\n")
print(retans)
if retstr !="":
    print(retstr)
# print(*dp,sep="\n")
