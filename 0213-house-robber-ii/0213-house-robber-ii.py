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

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)
        return max(self.memo(0,len(nums)-1,nums,dp1),self.memo(1,len(nums),nums,dp2))