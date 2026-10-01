class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        def backtrack(temp: List[int], i: int):
            answer.append(temp[:])
            for j in range(i,n):
                if j > i and nums[j] == nums[j-1]: continue
                temp.append(nums[j])
                backtrack(temp,j+1)
                temp.pop()
        backtrack([],0)
        return answer
             