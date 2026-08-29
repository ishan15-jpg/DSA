class Solution:
    def isPrefix(self, pref: str, word: str) -> bool:
        if len(pref) > len(word): return False
        i,j = 0,0
        while i < len(pref) and j < len(word):
            if pref[i] != word[j]: return False
            i += 1
            j += 1
        return True

    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if self.isPrefix(pref,word): res += 1
        return res