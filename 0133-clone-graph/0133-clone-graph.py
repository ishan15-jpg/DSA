"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        new_root = Node(val=node.val)
        mp = {node:new_root}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                mp[curr].neighbors.append(mp[neighbor])
        return new_root