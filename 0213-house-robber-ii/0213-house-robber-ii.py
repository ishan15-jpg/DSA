class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 3: return max(nums)
        next,next1 = 0,0
        for i in range(n-2,-1,-1):
            curr = max(next, next1+nums[i])
            next1,next = next,curr
        answer = curr
        next,next1 = 0,0 
        for i in range(n-1,0,-1):
            curr = max(next, nums[i]+next1)
            next1,next = next,curr
        return max(answer,next)