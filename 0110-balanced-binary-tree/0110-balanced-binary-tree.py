# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def helper(root):
            if not root:
                return 0

            left_depth = helper(root.left)
            right_depth = helper(root.right)
            if left_depth is False or right_depth is False:
                return False

            if abs(left_depth - right_depth) > 1:
                return False

            return max(left_depth, right_depth) + 1

        res = helper(root)
        return not res is False