func swap(nums []int, i int, j int){
    nums[i],nums[j] = nums[j],nums[i]
}

func rec(i int, n int, answer *[][]int, nums []int){
    if i == n {
        curr := make([]int, len(nums))
        copy(curr,nums)
        *answer = append(*answer, curr)
        return
    }
    for j:=i; j<n; j++ {
        swap(nums,i,j)
        rec(i+1,n,answer,nums)
        swap(nums,i,j)
    }
}

func permute(nums []int) [][]int {
    var answer [][]int
    rec(0,len(nums),&answer,nums)
    return answer
}