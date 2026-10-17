class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        counts = {}
        res = 0
        for t in time:
            normalized_time = t % 60
            res += counts.get((60-normalized_time) % 60, 0)
            counts[normalized_time] = counts.get(normalized_time, 0) + 1
        return res