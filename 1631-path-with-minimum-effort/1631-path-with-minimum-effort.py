class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        costs = [[math.inf] * n for _ in range(m)]
        costs[0][0] = 0
        queue = [(0, 0, 0)]

        while queue:
            cost, i, j = heappop(queue)

            for di, dj in diff:
                if 0 <= i+di < m and 0 <= j+dj < n:
                    neighbor_cost = max(cost, abs(heights[i][j] - heights[i+di][j+dj]))
                    if neighbor_cost < costs[i+di][j+dj]:
                        costs[i+di][j+dj] = neighbor_cost
                        heappush(queue, (neighbor_cost, i+di, j+dj))
        
        return costs[-1][-1]


