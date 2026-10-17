# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        m = {}

        max_i = 0
        while root and queue:
            root, i = queue.popleft()
            m[i] = m.get(i, []) + [root.val]
            if root.left:
                queue.append((root.left, i+1))
                max_i = max(max_i, i+1)
            if root.right:
                queue.append((root.right, i+1))
                max_i = max(max_i, i+1)
        
        return [m.get(i) for i in range(0, max_i + 1)]

        


            



        