class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_ = nums[0]
        for num in nums[1:]:
            curr = max(num,curr+num)
            max_ = max(max_,curr)
        return max_