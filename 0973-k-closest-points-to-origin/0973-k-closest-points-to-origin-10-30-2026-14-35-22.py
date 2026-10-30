class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for p in points:
            heappush(distances, (p[0] ** 2 + p[1] ** 2, p))
        
        res = []
        for _ in range(k):
            res.append(heappop(distances)[1])
        return res