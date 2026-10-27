/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        return countGood(root, Integer.MIN_VALUE);
    }

    private int countGood(TreeNode node, int max) {
        if (node == null) return 0;
        return  countGood(node.left, Math.max(node.val, max)) + 
                countGood(node.right, Math.max(node.val, max)) + 
                (node.val >= max ? 1 : 0);
    }
}