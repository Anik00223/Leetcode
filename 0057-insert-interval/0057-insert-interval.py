class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:

            # New interval is completely after current interval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # New interval is completely before current interval
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval

            # Intervals overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result