class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length, cols = board.length;

        int[] rows_ = new int[9], cols_ = new int[9], squares = new int[9];

        for(int r=0; r<rows; ++r){
            for(int c=0; c<cols; ++c){
                if(board[r][c] == '.') continue;
                int val = (board[r][c] - '0') - 1;
                int square = (r / 3) * 3 + (c / 3);
                if(((1 << val) & rows_[r]) > 0
                || ((1 << val) & cols_[c]) > 0
                || ((1 << val) & squares[square]) > 0
                ) return false;  

                rows_[r] |= (1 << val);
                cols_[c] |= (1 << val);
                squares[square] |= (1 << val);
            }
        }

        return true;
    }
}