class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 3: return max(nums)
        
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+2)

        for i in range(n-2,-1,-1):
            dp1[i] = max(dp1[i+1], nums[i]+dp1[i+2])
        for i in range(n-1,0,-1):
            dp2[i] = max(dp2[i+1], nums[i]+dp2[i+2])

        return max(dp1[0],dp2[1])