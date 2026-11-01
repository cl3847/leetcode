class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def cond(k):
            return sum((n + k - 1) // k for n in piles) <= h

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if cond(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


