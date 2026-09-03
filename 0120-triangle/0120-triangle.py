class Solution:
    def rec(self, row: int, col: int, triangle: List[List[int]]) -> int:
        if row == len(triangle): return 0
        currCol = self.rec(row+1,col,triangle) 
        nextCol = self.rec(row+1,col+1,triangle) 
        return triangle[row][col] + min(currCol,nextCol)

    def memo(self, row: int, col: int, dp: List[List[int]], triangle: List[List[int]]) -> int:
        if row == len(triangle): return 0
        if dp[row][col] is not None: return dp[row][col]
        currCol = self.memo(row+1,col,dp,triangle) 
        nextCol = self.memo(row+1,col+1,dp,triangle)
        dp[row][col] = triangle[row][col] + min(currCol,nextCol)
        return dp[row][col]

    def tab(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i+1) for i in range(n+1)]
        for r in range(n-1,-1,-1):
            for c in range(len(triangle[r])-1,-1,-1):
                currCol,nextCol = dp[r+1][c],dp[r+1][c+1]
                dp[r][c] = triangle[r][c] + min(currCol,nextCol)
        return dp[0][0]
    
    def tabSO(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next = [0] * (n+1)
        for r in range(n-1,-1,-1):
            curr = [0] * (n+1)
            for c in range(len(triangle[r])-1,-1,-1):
                curr[c] = min(next[c],next[c+1]) + triangle[r][c]
            next = curr
        return next[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp = [[None] * (i+1) for i in range(n)]
        return self.tabSO(triangle)