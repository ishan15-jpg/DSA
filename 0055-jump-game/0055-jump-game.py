class Solution:
    def rec(self, i: int, nums: List[int]) -> bool:
        if i == len(nums)-1: return True
        if i < len(nums)-1 and nums[i] == 0: return False
        for j in range(1,nums[i]+1):
            if self.rec(i+j,nums): return True
        return False

    def memo(self, i: int, dp: List[int], nums: List[int]) -> bool:
        if dp[i] != -1: return dp[i] == 1
        if i == len(nums)-1: return True
        if nums[i] == 0: return False
        end = min(i+nums[i],len(nums)-1)
        for j in range(i+1,end+1):
            if self.memo(j,dp,nums):
                dp[i] = 1
                return True
        dp[i] = 0
        return False

    def tab(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * (n+1)
        dp[n-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,min(i+nums[i],n-1)+1):
                if dp[j] != -1:
                    if dp[j] == 1: 
                        dp[i] = 1
                        break
                dp[i] = 0
        return dp[0] == 1

    def canJump(self, nums: List[int]) -> bool:
        # return self.rec(0,nums)
        dp = [-1] * len(nums)
        return self.tab(nums)
