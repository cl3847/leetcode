class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # interval problems typically have a
        #   1) sort
        #   2) left -> right pass

        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                prev = prev if prev[1] < curr[1] else curr
                res += 1
            else:
                prev = curr
        return res