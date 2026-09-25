class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.upper, num)
        upper_min = heapq.heappop(self.upper)
        heapq.heappush_max(self.lower, upper_min)

        if len(self.lower)-1 > len(self.upper):
            lower_max = heapq.heappop_max(self.lower)
            heapq.heappush(self.upper, lower_max)


    def findMedian(self) -> float:
        m1 = self.lower[0]
        if len(self.lower) > len(self.upper):
            return m1
        
        m2 = self.upper[0]
        return (m1 + m2) / 2
  