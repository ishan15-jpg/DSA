class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def rec(i: int):
            if i == len(nums): 
                answer.append(nums[:])
                return 
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                rec(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        rec(0)
        return answer