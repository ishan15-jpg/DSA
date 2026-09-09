class Solution {
    private void swap(int[][] matrix, int i, int j){
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
    }

    private void reverse(int[] arr){
        int n = arr.length;
        for(int i=0; i<n/2; ++i){
            int temp = arr[i];
            arr[i] = arr[n-i-1];
            arr[n-i-1] = temp;
        }
    }

    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for(int i=0; i<n-1; ++i){
            for(int j=i+1; j<n; ++j)
                this.swap(matrix,i,j);
        }
        for(int i=0; i<n; ++i)
            this.reverse(matrix[i]);
    }
}