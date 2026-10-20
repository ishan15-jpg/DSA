class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        i = 0
        while i+1 < len(prices):
            valley = 0
            while i+1 < len(prices) and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i+1 < len(prices) and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            res += peak - valley
        return res