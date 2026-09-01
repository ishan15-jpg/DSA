# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def help(root: Optional[TreeNode], targetSum: int) -> bool:
            if not root: return False
            if root and not root.left and not root.right: return targetSum - root.val == 0 
            return help(root.left,targetSum-root.val) or help(root.right,targetSum-root.val)
        return help(root,targetSum)