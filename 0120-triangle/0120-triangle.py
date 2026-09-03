class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None] * (i+1) for i in range(n)]
        def memo(row: int, col: int) -> int:
            if row == n: return 0
            if dp[row][col] is not None: return dp[row][col]
            currCol = memo(row+1,col) 
            nextCol = memo(row+1,col+1)
            dp[row][col] = triangle[row][col] + min(currCol,nextCol)
            return dp[row][col]
        return memo(0,0)