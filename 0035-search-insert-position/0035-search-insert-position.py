class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo