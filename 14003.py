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

path = [1 for i in range(len(l))]
length = 0
for i in range(len(l)):
    if not ans:
        ans.append(l[i])
    elif l[i] > ans[-1]:
        target = len(l[:i+1]) -1 -l[:i+1][::-1].index(ans[-1])
        path[i] = path[target]+1
        ans.append(l[i])
    else:
        id = lower_bound(0,len(ans)-1,l[i])
        ans[id] = l[i]
        path[i] = path[id]
    length = max(path[i],length)
ret = []
for i in range(len(l)-1,-1,-1):
    if length == path[i]:
        ret.append(l[i])
        length-=1
print(*list(reversed(ret)),sep=" ")
