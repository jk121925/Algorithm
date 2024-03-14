import sys
input = sys.stdin.readline

n = int(input())
dic ={i : [] for i in range(1,n+1)}

for i in range(n-1):
    a,b = map(int, input().split(" "))
    dic[a].append(b)
    dic[b].append(a)

q= []
print(dic)
dp = [[0 for i in range(n+1)] for i in range(2)]
print(*dp,sep="\n")
for k,v in dic.items():
    if len(v) ==1:
        q.append(k)
        dp[0][k] = 1
print(q)
# print(*dp,sep="\n")

# def solve(s):
#     global n
#     dp[0][s] = 1
def solve():
    global n
    ans = []
    round =[]
    visit = [False for i in range(n+1)]
    while q:
        if all(visit[idx] for idx in range(1,n+1)):
            return ans
        leaf = q.pop(0)
        visit[leaf] = True
        for d in dic[leaf]:
            if not visit[d] and d not in round:
                for t in dic[leaf]:
                    visit[t] = True
                print(leaf,ans,q,d)
                round.append(d)
        
#     return ans
print(solve())



