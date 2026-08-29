class TrieNode: 
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, words: List[str]):
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.count += 1

    def prefixCount(self, pref: str) -> int:
        curr = self.root
        for p in pref: 
            if p not in curr.children: return 0
            curr = curr.children[p]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        root = Trie()
        root.add(words)
        return root.prefixCount(pref)