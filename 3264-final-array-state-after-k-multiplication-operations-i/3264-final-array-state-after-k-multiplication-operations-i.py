class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = list(zip(nums, range(len(nums))))
        heapq.heapify(h)

        for _ in range(k):
            n = heapq.heappop(h)
            nums[n[1]] *= multiplier
            heapq.heappush(h, (n[0] * multiplier, n[1]))
        
        return nums

            
