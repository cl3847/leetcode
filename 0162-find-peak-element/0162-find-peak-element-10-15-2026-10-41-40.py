class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        min = 0
        max = len(nums)
        mid = min + (max-min) // 2

        while (mid > 0 and nums[mid-1] > nums[mid]) or (mid < len(nums)-1 and nums[mid+1] > nums[mid]):
            if mid > 0 and nums[mid-1] > nums[mid]:
                max = mid
                mid = min + (max-min) // 2
            elif mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                min = mid+1
                mid = min + (max-min) // 2
        return mid