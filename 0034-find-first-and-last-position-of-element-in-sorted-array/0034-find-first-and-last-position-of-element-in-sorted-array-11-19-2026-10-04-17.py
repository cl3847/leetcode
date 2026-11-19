class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        if not nums:
            return res

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        if 0 <= lo < len(nums) and nums[lo] == target:
            res[0] = lo

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        if 0 <= lo-1 < len(nums) and nums[lo-1] == target:
            res[1] = lo - 1
            
        return res