class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = sum(x for x in range(1,n+1))
        numsSum = sum(x for x in nums)
        return sum_ - numsSum