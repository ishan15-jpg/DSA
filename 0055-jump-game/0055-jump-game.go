func canJump(nums []int) bool {
    var n int = len(nums)
    var goal int = 0
    for i:=0; i<n; i++ {
        if i > goal { return false }
        goal = max(goal,i+nums[i])
        if goal >= n-1 { return true }
    }
    return false
}