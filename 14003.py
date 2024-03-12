import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split(" ")))
ans =[]
def lower_bound(s,e,target):
    while s<e:
        mid = int((e+s)/2)
        if l[mid] <target:
            s = mid+1
        else:
            e = mid
    return s

for i in range(len(l)):
    if not ans:
        ans.append(l[i])
    elif l[i] > ans[-1]:
        ans.append(l[i])
    else:
        id = lower_bound(0,len(ans)-1,l[i])
        ans[id] = l[i]
print(*ans,sep=" ")
