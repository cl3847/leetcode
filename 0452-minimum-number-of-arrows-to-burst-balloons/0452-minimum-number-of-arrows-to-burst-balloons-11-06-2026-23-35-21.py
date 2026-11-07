class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        prev = points[0]
        res = 0
        for curr in points[1:]:
            if curr[0] > prev[1]:
                prev = curr
                res += 1
            if curr[0] <= prev[1]:
                prev[0] = curr[0]
            if curr[1] <= prev[1]:
                prev[1] = curr[1]
        return res + 1