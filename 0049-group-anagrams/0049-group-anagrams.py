class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in temp: 
                temp[key] = []
            temp[key].append(s)
        return list(temp.values())