class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        x = 0
        for n in nums:
            x ^= n

        set_bit = x & -x

        g1, g2 = [], []
        for n in nums:
            if n & set_bit:
                g1.append(n)
            else:
                g2.append(n)
        
        r1 = r2 = 0
        for n in g1:
            r1 ^= n
        for n in g2:
            r2 ^= n
    
        return [r1, r2]