func sumOfUnique(nums []int) int {
    var n int8 = int8(len(nums))

    var freq [101]int8

    var sum int = 0

    for i := range int(n) {
        if freq[nums[i]] == 0 {
            sum += nums[i]
            freq[nums[i]]++
        }else{
            if freq[nums[i]] == 1 {
                sum -= nums[i]
            }
            freq[nums[i]]++
        }
    }

    return sum
}