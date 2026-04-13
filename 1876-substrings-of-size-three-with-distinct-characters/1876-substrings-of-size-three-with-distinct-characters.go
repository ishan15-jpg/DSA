func countGoodSubstrings(s string) int {
    var n int = len(s)
    if n < 0 { return 0 }

    var count int = 0
    for i:=0; i<n-2; i++ {
        if s[i] != s[i+1] && s[i] != s[i+2] && s[i+1] != s[i+2] { count++ }
    }

    return count
}