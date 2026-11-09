class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def subsets_from(nums):
            if not nums:
                return [[]]

            prefixes = [[]]
            i = 0
            while i < len(nums) and nums[i] == nums[0]: 
                prefixes.append(nums[0:i+1])
                i += 1
            
            suffixes = subsets_from(nums[i:])
            res = []
            for pre in prefixes:
                for suf in suffixes:
                    res.append(pre + suf)
            return res
        
        return subsets_from(sorted(nums))


            
        