class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        total = res = 0
        for n in nums:
            total += n
            res += counts[total-k]
            counts[total] += 1
        return res