# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q,answer = deque([(root, root.val)]), 0

        while q:
            curr, max_so_far = q.pop()

            if curr.val >= max_so_far: answer += 1

            new_max = max(curr.val, max_so_far)

            if curr.left: q.append((curr.left, new_max))
            if curr.right: q.append((curr.right, new_max))

        return answer