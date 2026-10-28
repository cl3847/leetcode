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
    public int res;

    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);
        return this.res;
    }

    public int helper(TreeNode node, int k) {
        if (node == null) return k;
        k = helper(node.left, k);
        if (k-- == 1) this.res = node.val;
        else k = helper(node.right, k);
        return k;
    }
}