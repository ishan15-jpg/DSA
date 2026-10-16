class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval : interval[-1])
        n = 1
        end = intervals[0][-1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][-1]
                n += 1
        return len(intervals) - n