# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root: return ""
        def pre(root: TreeNode) -> str:
            if not root: return "N,"
            serTree = str(root.val) + ","
            serTree += pre(root.left)
            serTree += pre(root.right)
            return serTree
        serializedTree = pre(root)
        return serializedTree[:len(serializedTree)-1]

    def deserialize(self, data) -> TreeNode:
        if not data: return None
        i = 0
        data = data.split(',')
        def dfs(data: str) -> TreeNode:
            nonlocal i
            if i >= len(data): return None
            if data[i] == "N": return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs(data)
            i += 1
            node.right = dfs(data)
            return node
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))