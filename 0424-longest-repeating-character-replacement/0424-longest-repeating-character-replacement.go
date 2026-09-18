func characterReplacement(s string, k int) int {
    n,l := len(s),0
    res := 1
    count,maxF := make(map[byte]int),0
    for r := range n {
        count[s[r]]++
        maxF = max(maxF,count[s[r]])
        for r-l+1-maxF > k {
            count[s[l]]--
            l++
        }
        res = max(res,r-l+1)
    }
    return res
}