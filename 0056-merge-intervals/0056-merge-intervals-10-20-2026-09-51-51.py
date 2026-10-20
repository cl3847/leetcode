class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        prev = intervals[0]
        for curr in intervals[1:]:
            if curr[0] <= prev[1]: # merge them
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(prev)
                prev = curr
        return res + [prev]
