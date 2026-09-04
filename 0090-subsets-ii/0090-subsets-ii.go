func rec(i int, n int, nums []int, temp []int, answer *[][]int){
    if i == n {
        var exists bool = slices.ContainsFunc(*answer, func(a []int) bool { 
            return slices.Equal(a, temp)
        }) 
        if !exists {
            dup := make([]int,len(temp))
            copy(dup,temp)
            *answer = append(*answer, dup)
        }
        return
    }
    temp = append(temp,nums[i])
    rec(i+1,n,nums,temp,answer)
    temp = temp[:len(temp)-1]
    rec(i+1,n,nums,temp,answer)
}

func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums[:])
    var temp []int
    var answer [][]int
    rec(0,len(nums),nums,temp,&answer)
    return answer
}