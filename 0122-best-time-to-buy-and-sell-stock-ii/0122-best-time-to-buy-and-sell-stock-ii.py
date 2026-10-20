class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(0,prices[i+1]-prices[i]) for i in range(len(prices)-1))