import sys
input = sys.stdin.readline

n = int(input())
l = [list(input().strip()) for i in range(n)]
dic = {}
for alphas in l:
    for idx, alpha in enumerate(alphas):
        square = len(alphas)-1
        if alpha not in dic.keys():
            dic[alpha] = 10**(square-idx)
        else:
            dic[alpha] += 10**(square-idx)

order = list(dic.items())
order.sort(key= lambda x : x[1], reverse=True)
ans = 0
for idx,o in enumerate(order):
    ans += o[1]  * (9-idx)
print(ans)
