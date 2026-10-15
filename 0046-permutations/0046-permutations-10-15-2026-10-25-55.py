class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i, n in enumerate(nums):
            permutations = self.permute(nums[:i] + nums[i+1:])
            res.extend([[n] + p for p in permutations])
        return res