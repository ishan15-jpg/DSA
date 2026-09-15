class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        leftMax,rightMax = 0,0
        res = 0
        while l < r:
            if height[l] <= height[r]:
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
                r -= 1
        return res