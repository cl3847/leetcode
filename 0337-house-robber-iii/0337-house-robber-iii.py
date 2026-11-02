# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        # [take this node, skip this node]
        if root is None: return (0, 0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        return (
            max(root.val + left[1] + right[1], left[0] + right[0]),
            left[0] + right[0]
        )

    def rob(self, root: TreeNode | None) -> int:
        return max(self.helper(root))