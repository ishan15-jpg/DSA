func findContentChildren(g []int, s []int) int {
    if len(s) == 0 { return 0 }
    slices.Sort(g)
    slices.Sort(s)
    i,j := 0,0
    res := 0
    for i < len(s) && j < len(g) {
        if s[i] >= g[j] {
            res += 1
            j += 1
        }
        i += 1
    }
    return res
}