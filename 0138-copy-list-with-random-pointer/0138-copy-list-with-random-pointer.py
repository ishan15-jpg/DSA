"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.copies = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        temp = head
        while head:
            self.copies[head] = Node(head.val)
            head = head.next
        head = temp
        while head:
            self.copies[head].next = self.copies[head.next] if head.next else None
            self.copies[head].random = self.copies[head.random] if head.random else None
            head = head.next
        return self.copies[temp]