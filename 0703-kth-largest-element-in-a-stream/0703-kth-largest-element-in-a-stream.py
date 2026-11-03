class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minheap = nums
        heapify(self.minheap)
        self.maxheap = []
        self.k = k

        while len(self.minheap) >= self.k:
            heappush_max(self.maxheap, heappop(self.minheap))


    def add(self, val: int) -> int:
        heappush(self.minheap, val)
        if len(self.minheap) >= self.k:
            heappush_max(self.maxheap, heappop(self.minheap))
        return self.maxheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)