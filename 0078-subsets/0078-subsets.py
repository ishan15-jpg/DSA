class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 : return [[], [nums[0]]]
        res, n = [[]], len(nums)

        for num in nums:
            res += [subset + [num] for subset in res]

        return res