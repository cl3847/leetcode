class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 0:
                mid -= 1

            print(nums[lo:hi])
            print(nums[mid], nums[mid+1])

            if nums[mid] == nums[mid+1]:
                hi = mid 
            else:
                lo = mid + 2
        return nums[lo if lo % 2 == 0 else lo - 1]