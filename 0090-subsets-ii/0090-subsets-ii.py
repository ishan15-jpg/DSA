class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        def backtrack(temp: List[int], i: int):
            if i >= n:
                answer.append(temp[:])
                return
            temp.append(nums[i])
            backtrack(temp,i+1)
            temp.pop()
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(temp,i+1)
        backtrack([],0)
        return answer
             