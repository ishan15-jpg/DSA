# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, max_so_far: int) -> int:
            if not root : return 0

            if root.val >= max_so_far : return 1 + dfs(root.left,root.val) + dfs(root.right,root.val)

            return dfs(root.left,max_so_far) + dfs(root.right,max_so_far)

        return dfs(root, root.val)