# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    moves = 0

    def distribute(self, root):
        if root is None:
            return 0
        l = self.distribute(root.left)
        r = self.distribute(root.right)
        excess = l + r + root.val - 1
        self.moves += abs(r) + abs(l)
        return excess

    def distributeCoins(self, root: TreeNode | None) -> int:
        self.distribute(root)
        return self.moves