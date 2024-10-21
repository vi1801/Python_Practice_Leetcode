# You are given n items, each with a weight and a value. You are also given a maximum weight capacity W.
# Find the maximum value that can be obtained without exceeding the weight capacity.
def knapsack(values, weights, w):
    n = len(values)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, w+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][w]

    return dp[n][j]


values = [60, 100, 120]
weights = [10, 20, 30]
w = 50
print(knapsack(values, weights, w))
