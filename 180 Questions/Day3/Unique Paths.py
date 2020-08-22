def uniquePaths(m, n):
    if m == n == 1:
        return 1
    dp = [[1 for i in range(m)] for j in range(n)]
    for row in range(1,n):
        for col in range(1,m):
            dp[row][col] = dp[row][col-1] + dp[row-1][col]
    return dp[-1][-1]

m = int(input())
n = int(input())
print(uniquePaths(m,n))


        