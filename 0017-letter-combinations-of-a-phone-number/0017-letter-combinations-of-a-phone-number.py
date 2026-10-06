class Solution:
    def __init__(self):
        self.mp = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        def backtrack(i: int, temp: str):
            if i == len(digits):
                res.append(temp)
                return
            for m in self.mp[digits[i]]:
                backtrack(i+1,temp+m)
        backtrack(0,"")
        return res