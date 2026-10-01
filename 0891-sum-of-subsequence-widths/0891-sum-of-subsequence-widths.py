class Solution:
    def sumSubseqWidths(self, nums):
        nums.sort()

        n = len(nums)
        MOD = 10**9 + 7

        # powers[i] = 2^i
        powers = [1] * n

        for i in range(1, n):
            powers[i] = powers[i - 1] * 2 % MOD

        answer = 0

        for i in range(n):
            # nums[i] is maximum in some subsequences
            maximum = powers[i]

            # nums[i] is minimum in some subsequences
            minimum = powers[n - i - 1]

            answer += nums[i] * (maximum - minimum)
            answer %= MOD

        return answer