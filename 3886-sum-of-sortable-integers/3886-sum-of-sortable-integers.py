class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)

        # Prefix maximum
        pref_max = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref_max[i + 1] = max(pref_max[i], x)

        # Suffix minimum
        suff_min = [10**9] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Count decreases between adjacent elements
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (nums[i - 1] > nums[i])

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                drops = pref_drop[end] - pref_drop[start]

                # Check the circular boundary
                if nums[end] > nums[start]:
                    drops += 1

                # Block must be sortable by rotation,
                # and blocks must join in sorted order.
                if drops > 1 or pref_max[start] > suff_min[start]:
                    return False

            return True

        answer = 0
        k = 1

        # Check divisors of n
        while k <= n // k:
            if n % k == 0:
                if check(k):
                    answer += k

                other = n // k
                if other != k and check(other):
                    answer += other

            k += 1

        return answer