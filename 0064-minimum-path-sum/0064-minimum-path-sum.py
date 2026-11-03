class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                up = left = inf
                if i > 0: up = dp[i-1][j]
                if j > 0: left = dp[i][j-1]
                dp[i][j] = min(up, left) + grid[i][j]
        return dp[-1][-1] 
