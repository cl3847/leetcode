class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        counts = [0] * k
        counts[0] = 1

        res = total = 0
        for n in nums:
            total = (total + n) % k
            res += counts[total]
            counts[total] += 1 
        return res