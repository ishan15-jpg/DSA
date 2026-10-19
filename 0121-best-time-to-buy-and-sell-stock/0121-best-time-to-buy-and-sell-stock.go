func maxProfit(prices []int) int {
    min_,res := prices[0],0
    for _,p := range prices {
        res = max(res, p-min_)
        min_ = min(min_, p)
    }
    return res
}