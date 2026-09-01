# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2: return root1 if not root2 else root2
        def help(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            root1.val = root1.val + root2.val
            if root1.left and root2.left: help(root1.left,root2.left)
            if root1.right and root2.right: help(root1.right,root2.right)
            if not root1.left:
                root1.left,root2.left = root2.left,None
            if not root1.right:
                root1.right,root2.right = root2.right,None
        help(root1,root2)
        return root1