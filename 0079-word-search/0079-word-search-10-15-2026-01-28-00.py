class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(x, y, i, seen):
            if (x,y) in seen:
                return False
            elif not (0 <= x < m) or not (0 <= y < n):
                return False
            elif not board[x][y] == word[i]:
                return False
            elif i == len(word) - 1:
                return True
            else:
                seen.add((x,y))
                res = dfs(x+1, y, i+1, seen) or dfs(x-1, y, i+1, seen) or dfs(x, y+1, i+1, seen) or dfs(x, y-1, i+1, seen)
                seen.remove((x,y))
                return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False