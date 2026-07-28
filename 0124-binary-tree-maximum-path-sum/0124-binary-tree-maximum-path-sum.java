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

    private int getMax(TreeNode root){
        if(root == null) return 0;
        int leftMax = getMax(root.left);
        int rightMax = getMax(root.right);
        return Math.max(0, root.val + Math.max(leftMax,rightMax));
    }

    public int maxPathSum(TreeNode root) {
        if(root == null) return 0;

        int leftSubMax = Math.max(getMax(root.left), 0);
        int rightSubMax = Math.max(getMax(root.right), 0);

        this.maxPathSum = Math.max(this.maxPathSum, leftSubMax + rightSubMax + root.val);

        maxPathSum(root.left);
        maxPathSum(root.right);

        return this.maxPathSum;
    }
}