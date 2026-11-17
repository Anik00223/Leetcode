
class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = 10**9

        # Step 1: Find all proper divisors
        factors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                factors[length].append(d)

        # Step 2: Calculate cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in factors[length]:
                    changes = 0

                    for offset in range(d):
                        left = i + offset
                        right = j - d + 1 + offset

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Step 3: Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):
                for end in range(i + 1, n):
                    if dp[end + 1][parts - 1] != INF:
                        dp[i][parts] = min(
                            dp[i][parts],
                            cost[i][end] + dp[end + 1][parts - 1]
                        )

        return dp[0][k]
