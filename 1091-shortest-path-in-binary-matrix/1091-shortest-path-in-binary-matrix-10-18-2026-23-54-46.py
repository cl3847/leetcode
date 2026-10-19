class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)]) if grid[0][0] == 0 else deque()
        seen = set((0, 0))
        i = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == m-1 and y == n-1:
                    return i
                for mod_x in (-1, 0, 1):
                    if not 0 <= x + mod_x < m:
                        continue
                    for mod_y in (-1, 0, 1):
                        if not 0 <= y + mod_y < n:
                            continue
                        if grid[x + mod_x][y + mod_y] == 0 and (x+mod_x, y+mod_y) not in seen:
                            queue.append((x+mod_x, y+mod_y))
                            seen.add((x+mod_x, y+mod_y))
            i += 1
        return -1
                
                            



