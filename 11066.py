for _ in range(int(input())):
    n = int(input())
    l = [0]+list(map(int, input().split(" ")))

    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n):
        dp[i][i+1] = l[i] + l[i+1]
    # print(*dp,sep="\n")
    # print()
    sum = [0]*(n+1)
    sum[1] = l[1]
    for i in range(1,n+1):
        sum[i] = sum[i-1]+l[i]
    # print(sum)
    # print()
    for length in range(1,n+1):
        for start in range(1,n-length+1):
            pivot = length + start
            dp[start][pivot] = 1e9
            for p in range(start,pivot):
                dp[start][pivot] = min(dp[start][pivot], dp[start][p] +dp[p+1][pivot] + sum[pivot]-sum[start-1])
    print(dp[1][-1])
