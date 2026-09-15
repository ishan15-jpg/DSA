class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    h = min(left,height[i]) - mid
                    w = i - stack[-1] - 1
                    res += h*w
            stack.append(i)
        return res