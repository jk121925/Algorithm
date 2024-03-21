import heapq
input = sys.stdin.readline

N,M = map(int,input().split(" "))

dic = {i:[] for i in range(N+1)}

for _ in range(M):
    a,b,c = map(int, input().split(" "))
    dic[a].append((c,b,a))
    dic[b].append((c,a,b))

ans =[]

q = []
visit = [False for i in range(N+1)]
heapq.heappush(q,(0,1))

while q:
    now = heapq.heappop(q)
    if visit[now[1]] ==True:
        continue
    visit[now[1]] = True
    ans.append(now)
    for d in dic[now[1]]:
        if visit[d[1]] ==False:
            heapq.heappush(q,d)
print(len(ans)-1)
ans_process = ans[1:]
ans_process = list(map(lambda x : str(x[1]) +" "+ str(x[2]), ans_process))
print(*ans_process,sep="\n")
