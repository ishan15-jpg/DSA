func maxProfit(prices []int) int {
    res,min_ := 0,prices[0]
    for i := range prices {
        res = max(res,prices[i]-min_)
        min_ = min(min_,prices[i])
    }
    return res
}