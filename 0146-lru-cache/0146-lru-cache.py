class Node:
    def __init__(self, key: int, value: int): 
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next,self.right.prev = self.right,self.left
        self.capacity = capacity
        self.mp = {}

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def insert(self, node: Node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node
        node.prev.next = node

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        self.remove(self.mp[key])
        self.insert(self.mp[key])
        return self.mp[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        elif len(self.mp) == self.capacity:
            del self.mp[self.left.next.key]
            self.remove(self.left.next)
        self.mp[key] = Node(key,value)
        self.insert(self.mp[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)