func swap(matrix [][]int, i int, j int) {
    var temp int = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp
}

func reverse(arr []int){
    var n int = len(arr)
    for i:=0; i<n/2; i++ {
        var temp int = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    }
}

func rotate(matrix [][]int)  {
    var n int = len(matrix)
    for i:=0; i<n-1; i++ {
        for j:=i+1; j<n; j++ {
            swap(matrix,i,j)
        }
    }
    for i:=0; i<n; i++ {
        reverse(matrix[i])
    }
}