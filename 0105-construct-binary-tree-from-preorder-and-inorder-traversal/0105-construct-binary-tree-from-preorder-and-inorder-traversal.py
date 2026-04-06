# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder) 

        if n == 1: return TreeNode(preorder[0])

        in_map = {val: idx for idx, val in enumerate(inorder)}

        pre_iter = iter(preorder)

        def help(start: int, end: int) -> Optional[TreeNode]:
            if start > end: return None

            root_val = next(pre_iter)
            root = TreeNode(root_val)

            idx  = in_map[root_val]

            root.left = help(start, idx-1)
            root.right = help(idx+1, end)

            return root

        return help(0, n-1)
