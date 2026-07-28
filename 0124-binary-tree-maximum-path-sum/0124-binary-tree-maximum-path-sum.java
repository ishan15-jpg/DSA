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
    private int maxPathSum = Integer.MIN_VALUE;

    private int help(TreeNode root){
        if(root == null) return 0;

        int leftMax = Math.max(this.help(root.left),0);
        int rightMax = Math.max(this.help(root.right),0);

        this.maxPathSum = Math.max(this.maxPathSum, root.val + leftMax + rightMax);

        return Math.max(0, root.val + Math.max(leftMax, rightMax));
    }

    public int maxPathSum(TreeNode root) {
        this.help(root);
        return this.maxPathSum;
    }
}