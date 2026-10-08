# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, max_left, max_right, best):
            if not root:
                return (-1, -1, -1)
            else:
                left = helper(root.left, max_left, max_right, best)
                right = helper(root.right, max_left, max_right, best)

                max_left = max(left[0], left[1]) + 1
                max_right = max(right[0], right[1]) + 1

                best = max(best, left[2], right[2], max_left + max_right)

                return (max_left, max_right, best)
        
        return helper(root, 0, 0, 0)[2]