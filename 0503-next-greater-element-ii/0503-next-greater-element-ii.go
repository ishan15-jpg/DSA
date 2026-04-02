func nextGreaterElements(nums []int) []int {
    var n int16 = int16(len(nums))

    answer := make([]int, int(n))

    st := make([]int, 0)
    var stLen int16 = 0

    for i:=2*n-1; i>=0; i-- {
        var curr int = nums[int(i%n)]

        for stLen > 0 && curr >= st[stLen-1] { 
            st = st[:int(stLen-1)]
            stLen--
        }

        if i < n {
            if stLen > 0 {
                answer[int(i)] = st[int(stLen-1)]
            }else {
                answer[int(i)] = -1
            }
        }

        st = append(st, curr)
        stLen++
    }
   
    return answer
}