func trap(height []int) int {
    l,r := 0,len(height)-1
    leftMax,rightMax := 0,0
    res := 0
    for l < r {
        if height[l] <= height[r] {
            leftMax = max(leftMax,height[l])
            res += leftMax - height[l]
            l++
        } else {
            rightMax = max(rightMax,height[r])
            res += rightMax - height[r]
            r--
        }
    }
    return res
}