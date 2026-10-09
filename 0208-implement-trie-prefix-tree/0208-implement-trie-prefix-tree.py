class TrieNode:
    def __init__(self):
        self.characters = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        while word: 
            c = word[0]
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
            word = word[1:]
        cur.is_terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        while word:
            c = word[0]
            if c not in cur.characters: return False
            cur = cur.characters[c]
            word = word[1:]
        return cur.is_terminal

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        while prefix:
            p = prefix[0]
            if p not in cur.characters: return False
            cur = cur.characters[p]
            prefix = prefix[1:]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)