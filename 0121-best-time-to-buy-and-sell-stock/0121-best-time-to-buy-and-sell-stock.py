class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        res,min_ = 0,prices[0]
        for i in range(1,n):
            res = max(res,prices[i]-min_)
            min_ = min(min_,prices[i])
        return res