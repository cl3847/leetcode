class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def ok(k):
            return sum([(x-1)//k + 1 for x in nums]) <= threshold

        lo = 1
        hi = max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
