class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length, cols = board[0].length;

        int[][] rows_ = new int[10][10], cols_ = new int[10][10], squares = new int[9][10];

        for(int r=0; r<rows; ++r){
            for(int c=0; c<cols; ++c){
                if(board[r][c] == '.') continue;
                int square = (r / 3) * 3 + (c / 3); 
                if(rows_[r][board[r][c] - '0'] == 1 
                || cols_[c][board[r][c] - '0'] == 1
                || squares[square][board[r][c] - '0'] == 1) return false;

                ++rows_[r][board[r][c] - '0'];
                ++cols_[c][board[r][c] - '0'];
                ++squares[square][board[r][c] - '0'];
            }
        }

        return true;
    }
}