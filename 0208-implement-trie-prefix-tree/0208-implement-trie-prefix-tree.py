class TrieNode:
    def __init__(self):
        self.child = {}
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def insertUtil(word: str, root: TrieNode) -> None:
            if len(word) == 0:
                root.isTerminal = True
                return
            key = word[0]
            if key not in root.child:
                root.child[key] = TrieNode()
            insertUtil(word[1:], root.child[key])
        insertUtil(word, self.root)

    def search(self, word: str) -> bool:
        def searchUtil(word: str, root: TrieNode) -> bool:
            if not len(word): return root.isTerminal
            key = word[0]
            if key not in root.child: return False
            return searchUtil(word[1:], root.child[key])
        return searchUtil(word, self.root)

    def startsWith(self, prefix: str) -> bool:
        def startsWithUtil(prefix: str, root: TrieNode) -> bool:
            if not len(prefix): return True
            key = prefix[0]
            if key not in root.child: return False
            return startsWithUtil(prefix[1:], root.child[key])
        return startsWithUtil(prefix, self.root)        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)