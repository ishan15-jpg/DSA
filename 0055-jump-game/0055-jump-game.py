class Solution:
    def rec(self, i: int, nums: list[int]) -> bool:
        if i >= len(nums)-1: return True
        if i < len(nums)-1 and nums[i] == 0: return False
        for j in range(1,nums[i]+1):
            if i+j <= len(nums)-1 and self.rec(i+j, nums): return True
        return False

    def memo(self, i: int, dp: list[int], nums: list[int]) -> bool:
        if i >= len(nums)-1: return True
        if i < len(nums)-1 and nums[i] == 0: return False
        if dp[i] != None: return dp[i]
        res = False
        for step in range(1,nums[i]+1):
            if i+step <= len(nums) and self.memo(i+step,dp,nums):
                res = True
                break
        dp[i] = res
        return dp[i]

    def tab(self, nums: list[int]) -> bool:
        dp = [None] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                dp[i] = False
                continue
            res = False
            for step in range(1,nums[i]+1):
                if i+step <= len(nums)-1 and dp[i+step]: 
                    res = True
                    break
            dp[i] = res
        return dp[0]

    def canJump(self, nums: list[int]) -> bool:
        dp = [None] * len(nums)
        return self.tab(nums)