# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q):
            if not node: return False

            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            is_match = node == p or node == q

            if (left and right) or ((left or right) and is_match):
                self.res = node
                return True

            return left or right or is_match

        self.res = root
        helper(root, p, q)
        return self.res
    
    


        