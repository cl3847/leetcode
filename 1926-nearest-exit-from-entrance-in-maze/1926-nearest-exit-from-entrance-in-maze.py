class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(maze), len(maze[0])
        queue = deque([entrance])
        steps = 0
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while queue:
            for _ in range(len(queue)):
                cx, cy = queue.popleft()

                if (cx == 0 or cx == m-1 or cy == 0 or cy == n-1) and [cx, cy] != entrance:
                    return steps
                for dx, dy in MOVES:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                        queue.append([cx+dx, cy+dy])
                        visited.add((nx, ny))
            
            steps += 1

        return -1

            