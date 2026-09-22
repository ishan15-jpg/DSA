func findDuplicate(nums []int) int {
    n := len(nums)
    mp := make([]int,n+1)
    for _,num := range nums {
        if mp[num] == 1 { return num }
        mp[num]++
    }
    return -1
}