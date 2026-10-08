class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(grid, m, n):
            if grid[m][n] == "0":
                return
            grid[m][n] = "0"
            if m > 0:
                explore(grid, m - 1, n)
            if m < len(grid) - 1:
                explore(grid, m + 1, n)
            if n > 0:
                explore(grid, m, n - 1)
            if n < len(grid[0]) - 1:
                explore(grid, m, n + 1)

        count = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    count += 1
                    explore(grid, m, n)
        
        return count

            
