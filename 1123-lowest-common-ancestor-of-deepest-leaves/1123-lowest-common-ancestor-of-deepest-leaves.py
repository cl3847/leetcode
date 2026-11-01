# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def helper(node, depth):
            if node == None:
                return (depth, None)
            
            ld, left = helper(node.left, depth + 1)
            rd, right = helper(node.right, depth + 1)
            
            if ld == rd:
                return (ld, node)
            elif ld < rd:
                return (rd, right)
            elif ld > rd:
                return (ld, left)

        return helper(root, 0)[1]
            

            