# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def inOrder(root: Optional[TreeNode]) -> int:
            if not root: return 
            inOrder(root.left)
            inorder.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return inorder[k-1]