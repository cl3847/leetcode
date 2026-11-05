class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_counts = defaultdict(int)
        odd_counts[0] = 1
        res = count = 0
        for n in nums:
            if n % 2 == 1:
                count += 1
            res += odd_counts[count-k]
            odd_counts[count] += 1
        return res