func longestConsecutive(nums []int) int {
    mp := make(map[int]int)
    res := 0
    for _,num := range nums {
        if _,ok := mp[num]; !ok {
            left,right := 0,0
            if _,ok := mp[num-1]; ok {
                left = mp[num-1]
            }
            if _,ok := mp[num+1]; ok {
                right = mp[num+1]
            }
            mp[num] = left + right + 1
            mp[num-left] = mp[num]
            mp[num+right] = mp[num] 
            res = max(res,mp[num])
        }
    }
    return res
}