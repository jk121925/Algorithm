import sys
import heapq
input = sys.stdin


n,m = map(int, input.readline().split(" "))
vw = []
for _ in range(n):
    w,v = map(int, input.readline().split(" "))
    vw.append((w,v))

bags = []
for i in range(m):
    bags.append(int(input.readline()))
bags.sort()
vw.sort()
print(vw)
print(bags)
ans = 0
q=[]
t=0
for b in bags:
    while t <=len(vw)-1 and b >=vw[t][0]:
        heapq.heappush(q,-vw[t][1])
        t+=1
    print(q)
    if q:
        ans += -heapq.heappop(q)
        print(ans)
print(ans)
