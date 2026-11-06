class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        counts = [0, 0]
        res = 0
        l = 0
        for r, n in enumerate(nums):
            counts[n] += 1
            if (r - l + 1) - counts[1] > k:
                counts[nums[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res


        