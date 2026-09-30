class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []
        candidates.sort()
        def backtrack(temp: List[int], target: int, start: int):
            if target == 0:
                answer.append(temp[:])
                return 
            for i in range(start,len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtrack(temp, target-candidates[i], i+1)
                temp.pop()
        backtrack([],target,0)
        return answer