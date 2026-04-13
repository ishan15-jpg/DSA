func applyOperations(nums []int) []int {
    var n int16 = int16(len(nums))

    for i := range int(n-1) {
        if nums[i] == nums[i+1] {
            nums[i] *= 2
            nums[i+1] = 0
        }
    }

    var j int16 = 0
    for i := range int(n) {
        if nums[i] != 0 {
            nums[i], nums[j] = nums[j], nums[i]
            j++
        }
    }

    return nums
}