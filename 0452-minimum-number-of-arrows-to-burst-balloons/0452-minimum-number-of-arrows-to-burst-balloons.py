class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda point:point[1])
        res = 1
        end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > end:
                end = points[i][-1]
                res += 1
        return res