func maxSubArray(nums []int) int {
    var curr int = nums[0]
    var max_ int = nums[0]
    for i:=1; i<len(nums); i++ {
        curr = max(curr+nums[i],nums[i])
        max_ = max(curr,max_)
    }
    return max_
}