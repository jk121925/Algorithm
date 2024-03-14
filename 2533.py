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
visit = [False for i in range(n+1)]
def solve(s):
    # 0은 내가 얼리어답터
    dp[0][s] = 1
    visit[s] = True
    for d in dic[s]:
        if not visit[d]:
            solve(d)
            dp[0][s] += min(dp[1][d], dp[0][d])
            dp[1][s] += dp[0][s]

print(solve())



