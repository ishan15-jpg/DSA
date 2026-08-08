class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 3: return max(nums)
        dp = [[-1]*2 for _ in range(len(nums))]
        def rec(i: int, flag: bool) -> int:
            if i >= n or (flag and i == len(nums)-1): return 0
            if dp[i][flag] != -1: return dp[i][flag]
            dp[i][flag] = max(rec(i+1,flag), nums[i]+rec(i+2,flag))
            return dp[i][flag]
        return max(rec(0,True),rec(1,False))