class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def search(val):
            res = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == val:
                        res.append((i, j))
            return res

        queue = deque(search(2))
        minutes = -1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
            minutes += 1
        return max(minutes, 0) if not search(1) else -1
                
        

