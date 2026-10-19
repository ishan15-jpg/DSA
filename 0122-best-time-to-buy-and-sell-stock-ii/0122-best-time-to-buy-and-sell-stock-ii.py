class Solution:
    def rec(self, i: int, prices: list[int], holding: bool) -> int:
        if i == len(prices):
            return 0
        res = 0
        if holding:
            sell = prices[i] + self.rec(i+1, prices, False)
            skip = self.rec(i+1, prices, True)
            res = max(sell,skip)
        else:
            buy = self.rec(i+1, prices, True) - prices[i]
            skip = self.rec(i+1, prices, False)
            res = max(buy,skip)
        return res

    def memo(self, i: int, prices: list[int], holding: int, dp: list[int]) -> int:
        if i == len(prices):
            return 0
        if dp[i][holding] != -1: 
            return dp[i][holding]
        res = 0
        if holding:
            sell = prices[i] + self.memo(i+1,prices,0,dp)
            skip = self.memo(i+1,prices,1,dp)
            res = max(sell,skip)
        else:
            buy = self.memo(i+1,prices,1,dp) - prices[i]
            skip = self.memo(i+1,prices,0,dp)
            res = max(buy,skip)
        dp[i][holding] = res
        return res

    def tab(self, prices: list[int]) -> int:
        dp = [[0,0] for _ in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for holding in range(2):
                res = 0
                if holding:
                    sell = prices[i] + dp[i+1][0]
                    skip = dp[i+1][1]
                    res = max(sell,skip)
                else:
                    buy = dp[i+1][1] - prices[i]
                    skip = dp[i+1][0]
                    res = max(buy,skip)
                dp[i][holding] = res
        return dp[0][0]

    def maxProfit(self, prices: list[int]) -> int:
        dp = [[-1,-1] for _ in range(len(prices))]
        return self.tab(prices)