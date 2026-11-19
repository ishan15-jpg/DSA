class Solution:
    def rec(self, i: int, end: int, nums: list[int]) -> int:
        if i >= end: return 0
        rob = nums[i] + self.rec(i+2,end,nums)
        skip = self.rec(i+1,end,nums)
        return max(rob,skip)

    def memo(self, i: int, end: int, nums: list[int], dp: list[int]) -> int:
        if i >= end: return 0
        if dp[i] != -1: return dp[i]
        rob = nums[i] + self.memo(i+2,end,nums,dp)
        skip = self.memo(i+1,end,nums,dp)
        dp[i] = max(rob,skip)
        return dp[i]
    
    def tab(self, nums: list[int]) -> int:
        dp1 = [0] * (len(nums)+2)
        for i in range(len(nums)-1,0,-1):
            dp1[i] = max(nums[i]+dp1[i+2],dp1[i+1])
        dp2 = [0] * (len(nums)+2)
        for i in range(len(nums)-2,-1,-1):
            dp2[i] = max(nums[i]+dp2[i+2],dp2[i+1])
        return max(dp1[1],dp2[0])

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2: return max(nums)
        return self.tab(nums)