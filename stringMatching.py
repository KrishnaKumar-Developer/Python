def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    # Create a DP table to store the length of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS is dp[m][n]
    return dp[m][n]

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print(f"Length of LCS is {longest_common_subsequence(X, Y)}")
