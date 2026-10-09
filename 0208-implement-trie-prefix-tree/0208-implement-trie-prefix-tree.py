class TrieNode:
    def __init__(self):
        self.characters = {}
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def util(word: str, root: TrieNode) -> None:
            if len(word) == 0: 
                root.isTerminal = True
                return
            c = word[0]
            if c in root.characters:
                util(word[1:], root.characters[c])
            else:
                root.characters[c] = TrieNode()
                util(word[1:], root.characters[c])
        util(word, self.root)

    def search(self, word: str) -> bool:
        def util(word: str, root: TrieNode) -> bool:
            if len(word) == 0: return root.isTerminal == True
            c = word[0] 
            if c not in root.characters: return False
            return util(word[1:], root.characters[c])
        return util(word, self.root)
        
    def startsWith(self, prefix: str) -> bool:
        def util(prefix: str, root: TrieNode) -> bool:
            if len(prefix) == 0: return True
            p = prefix[0]
            if p not in root.characters: return False
            return util(prefix[1:], root.characters[p])
        return util(prefix, self.root)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)