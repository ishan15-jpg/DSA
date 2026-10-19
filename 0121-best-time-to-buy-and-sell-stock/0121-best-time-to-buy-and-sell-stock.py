class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_,res = prices[0],0
        for p in prices:
            res = max(res, p-min_)
            min_ = min(min_, p)
        return res
