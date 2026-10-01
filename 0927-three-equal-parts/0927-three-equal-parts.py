class Solution:
    def threeEqualParts(self, arr):
        ones = sum(arr)

        # Total number of 1s must be divisible by 3
        if ones % 3 != 0:
            return [-1, -1]

        # If there are no 1s, any split works
        if ones == 0:
            return [0, 2]

        k = ones // 3

        # Find the starting position of the 1s
        # in each of the three parts.
        starts = []
        count = 0

        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1

                if count == 1 or count == k + 1 or count == 2 * k + 1:
                    starts.append(i)

        i, j, z = starts

        # The three parts must have exactly the same
        # sequence from their first 1 onward.
        while z < len(arr):
            if arr[i] != arr[j] or arr[j] != arr[z]:
                return [-1, -1]

            i += 1
            j += 1
            z += 1

        # i and j are now the positions just after
        # the common binary sequence.
        return [i - 1, j]