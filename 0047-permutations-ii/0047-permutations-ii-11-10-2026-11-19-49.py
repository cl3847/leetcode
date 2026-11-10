class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        return self.permute(nums)

    def permute(self, nums):
        if nums[0] == nums[-1]:
            return [nums]
        
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]: 
                continue
            permutations = self.permute(nums[:i] + nums[i+1:])
            res.extend([[n] + p for p in permutations])
        return res

