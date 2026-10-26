class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurrence = {s[i]:i for i in range(len(s))}
        res = []
        for i in range(len(s)):
            if s[i] in res: continue
            while res and s[i] < res[-1] and i < lastOccurrence[res[-1]]:
                res.pop()
            res.append(s[i])
        return "".join(res)