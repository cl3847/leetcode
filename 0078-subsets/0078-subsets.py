class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        mask = 0
        res = []

        while mask < 2 ** len(nums):
            res.append([n for i, n in enumerate(nums) if (1 << i) & mask])
            mask += 1

        return res
            