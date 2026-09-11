func spiralOrder(matrix [][]int) []int {
    top,bottom := 0,len(matrix)-1
    left,right := 0,len(matrix[0])-1
    var answer []int
    for left <= right && top <= bottom {
        for i:=left; i<right+1; i++ {
            answer = append(answer,matrix[top][i])
        }
        top++
        for i:=top; i<bottom+1; i++ {
            answer = append(answer,matrix[i][right])
        }
        right--
        if left > right || top > bottom { break }
        for i:=right; i>left-1; i-- {
            answer = append(answer,matrix[bottom][i])
        } 
        bottom--
        for i:=bottom; i>top-1; i-- {
            answer = append(answer,matrix[i][left])
        }
        left++
    }
    return answer
}