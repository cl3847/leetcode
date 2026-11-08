# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        sums = []
        def walk(root):
            if root is None:
                return 0
            s = walk(root.left) + walk(root.right) + root.val
            sums.append(s)
            return s
        
        total = walk(root)
        res = 0
        for n in sums:
            res = max(res, (total-n) * n)

        return res % (10 ** 9 + 7)

        
            

            