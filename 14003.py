import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split(" ")))

def lower_bound(s,e,target):
    while s<e:
        mid = int((e+s)/2)
        if dp[mid] <target:
            s = mid+1
        else:
            e = mid
    return s

length = 0
dp = [-1000000000]
store =[]
for t in l:
    if t > dp[-1]:
        dp.append(t)
        store.append((len(dp)-1,t))
    else:
        index = lower_bound(0,len(dp)-1,t)
        dp[index] = t
        store.append((index,t))


length = len(dp)-1
ret =[]
print(length)
for i in range(len(l)-1,-1,-1):
    if length == store[i][0]:
        ret.append(store[i][1])
        length-=1

print(*ret[::-1],sep=" ")
