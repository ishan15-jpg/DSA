func checkInclusion(s1 string, s2 string) bool {
    l1,l2 := len(s1),len(s2)
    if l1 > l2 { return false }
    var count1, count2 [26]int
    for i := range l1 {
        count1[s1[i] - 'a']++
        count2[s2[i] - 'a']++
    }
    if count1 == count2 { return true }
    for i:=l1; i<l2; i++ {
        count2[s2[i] - 'a']++
        count2[s2[i - l1] - 'a']--
        if count2 == count1 { return true }
    }
    return false
}