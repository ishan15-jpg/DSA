# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        if n == 1: return TreeNode(postorder[0])

        inorder_map = { val: idx for idx, val in enumerate(inorder) }

        postorder.reverse()
        postorder_iter = iter(postorder)

        def help(start: int, end: int) -> Optional[TreeNode]:
            if start > end: return None

            root_val = next(postorder_iter)
            root = TreeNode(root_val)

            idx = inorder_map[root_val]

            root.right = help(idx+1, end)
            root.left = help(start, idx-1)

            return root
        
        return help(0, n-1)