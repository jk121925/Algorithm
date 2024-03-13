import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split(" ")))

def lower_bound(s,e,target):
    while s<e:
        mid = int((e+s)/2)
        if ans[mid][0] <target:
            s = mid+1
        else:
            e = mid
    return s

length = 0
dp =[[l[i],1] for i in range(len(l))]
ans=[]
for i in range(len(l)):
    if not ans:
        ans.append(dp[i])
    elif l[i] > ans[-1][0]:
        dp[i][1] = ans[-1][1]+1
        ans.append(dp[i])
    else:
        id = lower_bound(0,len(ans)-1,l[i])
        dp[i][1] = ans[id][1]
        ans[id] = dp[i]
    length = max(length,dp[i][1])
ret = ""
for i in range(len(l)-1,-1,-1):
    if length == dp[i][1]:
        ret = " " + str(dp[i][0]) + ret
        length-=1
print(ret.strip())
