class Solution:
    def rec(self, i: int, nums: list[int]) -> int:
        if i >= len(nums): return 0
        rob = nums[i] + self.rec(i+2,nums)
        skip = self.rec(i+1,nums)
        return max(rob,skip)

    def memo(self, i: int, nums: list[int], dp: list[int]) -> int:
        if i >= len(nums): return 0
        if dp[i] != -1: return dp[i]
        rob = nums[i] + self.memo(i+2,nums,dp)
        skip = self.memo(i+1,nums,dp)
        dp[i] = max(rob,skip)
        return dp[i]

    def tab(self, nums: list[int]) -> int:
        dp = [0] * (len(nums)+2)
        for i in range(len(nums)-1,-1,-1):
            rob = nums[i]+dp[i+2]
            skip = dp[i+1]
            dp[i] = max(rob,skip)
        return dp[0]

    def tabSO(self, nums: list[int]) -> int:
        next,next2 = 0,0
        for i in range(len(nums)-1,-1,-1):
            rob = nums[i]+next2
            skip = next
            next2 = next
            next = max(rob,skip)
        return next

    def rob(self, nums: list[int]) -> int:
        dp = [-1] * len(nums)
        return self.tabSO(nums)