# find a longest subsequence common to two sequences.

def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[m][n]


x = "taggable"
y = "gxtxayb"
print(lcs(x, y))
