class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, x - mid) for x in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left
        remaining = k

        for i in range(len(diff)):
            reduction = max(0, diff[i] - threshold)
            diff[i] -= reduction
            remaining -= reduction

        diff.sort(reverse=True)

        for i in range(min(remaining, len(diff))):
            if diff[i] > 0:
                diff[i] -= 1

        return sum(x * x for x in diff)