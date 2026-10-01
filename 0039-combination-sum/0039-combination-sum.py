class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        answer = []
        def backtrack(temp: List[int], i: int, target: int):
            if target == 0:
                answer.append(temp[:])
                return
            if i == n or target < 0: return
            temp.append(candidates[i])
            backtrack(temp,i,target-candidates[i])
            temp.pop()
            backtrack(temp,i+1,target)
        backtrack([],0,target)
        return answer