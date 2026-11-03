class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            s1 = heappop_max(stones)
            s2 = heappop_max(stones)

            if not s1 == s2:
                heappush_max(stones, abs(s2 - s1))
        return stones[0] if stones else 0