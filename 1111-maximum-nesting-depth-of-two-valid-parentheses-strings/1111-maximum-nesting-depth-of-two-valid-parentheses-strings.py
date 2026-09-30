class Solution:
    def maxDepthAfterSplit(self, seq):
        result = [0] * len(seq)
        level = 0

        for i, ch in enumerate(seq):
            if ch == '(':
                level += 1
                result[i] = level & 1
            else:
                result[i] = level & 1
                level -= 1

        return result