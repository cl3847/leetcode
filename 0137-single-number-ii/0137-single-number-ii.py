class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        times = {}
        for n in nums:
            times[n] = (times.get(n, 0) + 1) % 3

        for k in times.keys():
            if times[k] == 1:
                return k
        