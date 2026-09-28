class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            
            max_depth = max(max_depth, depth)
        return max_depth