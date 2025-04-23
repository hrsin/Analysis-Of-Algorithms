def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack_dp(weights, values, capacity)
print("Dynamic Programming Knapsack (0/1) -> Max value:", max_value)
