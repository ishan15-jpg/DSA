# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root: Optional[TreeNode]) -> tuple(int):
        if not root: return (0,0)
        leftT = self.help(root.left)
        rightT = self.help(root.right)
        return (max(leftT[0],rightT[0])+1, max(max(leftT[1],rightT[1]),leftT[0]+rightT[0]))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.help(root)[1]