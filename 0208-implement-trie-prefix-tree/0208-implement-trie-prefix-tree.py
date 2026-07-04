class TrieNode: 
    def __init__(self,value='\0'):
        self.value = value
        self.child = { i: None for i in range(27) }
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = len(word)
        def util(root: TrieNode, i: int) -> TrieNode:
            if i == n:
                root.isTerminal = True
                return
            idx = ord(word[i]) - ord('a')
            if not root.child[idx]:
                node = TrieNode(idx)
                root.child[idx] = node
                util(node,i+1)
            else:
                util(root.child[idx],i+1)
        util(self.root,0)
            
    def search(self, word: str) -> bool:
        n = len(word)
        def util(root: TrieNode, i: int) -> bool:
            if i == n: return root.isTerminal
            idx = ord(word[i]) - ord('a')
            if not root.child[idx]: return False
            return util(root.child[idx],i+1)
        return util(self.root,0)

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        def util(root: TrieNode, i: int) -> bool:
            if i == n: return True
            idx = ord(prefix[i]) - ord('a')
            if not root.child[idx]: return False
            return util(root.child[idx],i+1)
        return util(self.root,0)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)