class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations: C[i][j]
        C = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            C[i][0] = 1
            C[i][i] = 1

            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            combinations = C[len(left) + len(right)][len(left)]

            return (combinations * left_ways * right_ways) % MOD

        return (solve(nums) - 1) % MOD