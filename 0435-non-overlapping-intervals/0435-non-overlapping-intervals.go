func eraseOverlapIntervals(intervals [][]int) int {
    slices.SortFunc(intervals, func(a,b []int) int {
        return cmp.Compare(a[1],b[1])
    })
    n := 1
    end := intervals[0][1]
    for i:=1; i<len(intervals); i++ {
        if intervals[i][0] >= end {
            end = intervals[i][1]
            n++
        }
    }
    return len(intervals) - n
}