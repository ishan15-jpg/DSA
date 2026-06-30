# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -math.inf, math.inf)])

        while q:
            curr, min_, max_ = q.pop()

            if curr.val <= min_ or curr.val >= max_ : return False

            if curr.left : q.appendleft((curr.left, min_, curr.val))
            if curr.right : q.appendleft((curr.right, curr.val, max_))

        return True