class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        position = { c : i for i,c in enumerate(s) }
        res = []
        start,farthest = 0,0
        for i in range(len(s)):
            farthest = max(farthest,position[s[i]])
            if i == farthest:
                res.append(i-start+1)
                start = farthest+1
                farthest += 1
        return res