func twoSum(nums []int, target int) []int {
    var( 
        n uint16 = uint16(len(nums))
        i uint16 = 0    
    )
    answer := make([]int, 0)
    m := make(map[int]uint16)

    for i < n {
        var k int = target - nums[i]
        idx, exists := m[k]
        if exists {
            answer = append(answer, int(idx), int(i))
            break
        }
        m[nums[int(i)]] = i 
        i++
    }

    return answer
}