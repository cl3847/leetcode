class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def ok(k):
            return sum([math.ceil(x / k) for x in piles]) <= h

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
