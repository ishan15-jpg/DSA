class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    mp = defaultdict(list)
    for i in range(len(strs)):
      count = [0] * 26
      for c in strs[i]:
        count[ord(c) - ord('a')] += 1
      mp[tuple(count)].append(strs[i])
    res = []
    for _,v in mp.items():
      res.append(v)
    return res