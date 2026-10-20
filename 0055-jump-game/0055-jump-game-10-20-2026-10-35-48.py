class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        best = 0
        for i, n in enumerate(nums):
            if i > best: break
            best = max(best, i + n)
        return best >= len(nums) - 1