class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, seen):
            if (not 0 <= i < m) or (not 0 <= j < n):
                return 0
            elif grid[i][j] == 0:
                return 0
            elif (i,j) in seen:
                return 0
            else:
                seen.add((i, j))
                best = max(
                    dfs(i+1, j, seen),
                    dfs(i-1, j, seen),
                    dfs(i, j+1, seen),
                    dfs(i, j-1, seen)
                ) + grid[i][j]
                seen.remove((i, j))
                return best

        best = 0
        for i in range(m):
            for j in range(n):
                best = max(best, dfs(i, j, set()))
        return best