class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = 0
        target = sum(nums)
        for i, n in enumerate(nums):
            if 2 * total + n == target:
                return i
            total += n
        return -1