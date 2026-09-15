class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for num in nums:
            if num not in mp:
                left,right = mp.get(num-1,0),mp.get(num+1,0)
                mp[num] = left + right + 1
                mp[num - left] = mp[num]
                mp[num + right] = mp[num]
                res = max(res,mp[num])
        return res