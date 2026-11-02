# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        @cache
        def helper(node, can_take):
            if node is None:
                return 0

            totals = []
            if can_take:
                totals.append(helper(node.left, False) + helper(node.right, False) + node.val)
            totals.append(helper(node.left, True) + helper(node.right, True))

            return max(totals)

        return helper(root, True)