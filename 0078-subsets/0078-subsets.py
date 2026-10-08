class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        for mask in range(2 ** len(nums)):
            res.append([n for i, n in enumerate(nums) if (1 << i) & mask])
        return res
            