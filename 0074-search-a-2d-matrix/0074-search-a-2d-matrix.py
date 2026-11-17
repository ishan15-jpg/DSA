class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l,r = 0,len(matrix[0])*len(matrix) - 1
        while l<=r:
            mid = (l+r)>>1
            curr = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if curr == target: return True
            elif curr < target: l = mid+1
            else: r = mid-1
        return False 