class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        x = 0
        for n in nums:
            x ^= n

        set_bit = x & -x

        res = [0, 0]
        for n in nums:
            if n & set_bit:
                res[0] ^= n
            else:
                res[1] ^= n

        return res