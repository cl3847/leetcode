class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        counts = [0, 1]
        total = res = 0
        for n in arr:
            total += n
            if total % 2 == 0:
                res += counts[0]
                counts[1] += 1
            else:
                res += counts[1]
                counts[0] += 1
        return res % ((10 ** 9) + 7)


