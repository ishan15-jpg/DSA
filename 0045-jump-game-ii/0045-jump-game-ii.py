class Solution:
    def rec(self, i: int, nums: list[int]) -> int:
        if i == len(nums)-1: return 0
        res = float(inf)
        for step in range(1,nums[i]+1):
            if i+step <= len(nums):
                res = min(res,self.rec(i+step,nums))
        return res+1

    def memo(self, i: int, dp: list[int], nums: list[int]) -> int:
        if i == len(nums)-1: return 0
        if dp[i] != -1: return dp[i] 
        res = float(inf)
        for step in range(1,nums[i]+1):
            if i+step < len(nums):
                res = min(res,self.memo(i+step,dp,nums))
        dp[i] = res+1
        return dp[i]

    def tab(self, nums: list[int]) -> int:
        dp = [float(inf)] * len(nums)
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0: continue
            res = float(inf)
            for step in range(1,nums[i]+1):
                if i+step < len(nums):
                    res = min(res,dp[i+step])
            dp[i] = res + 1
        return dp[0]

    def jump(self, nums: list[int]) -> int:
        return self.tab(nums)