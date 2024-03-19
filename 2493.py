import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split(" ")))
ans = [0 for i in range(n)]
lefts = []
rights = []

for i in range(len(l)-1,-1,-1):
    if not lefts:
        lefts.append((l[i],i))
    else:
        if l[i] < lefts[-1][0]:
            lefts.append((l[i],i))
        else:
            while lefts:
                if l[i] < lefts[-1][0]:
                    break
                value,index = lefts.pop()
                ans[index] = i+1
            lefts.append((l[i],i))
print(ans)
