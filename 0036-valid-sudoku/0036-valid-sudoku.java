class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length, cols = board[0].length;

        for(int r=0; r<rows; ++r){
            int[] seen = new int[10];
            for(int c=0; c<cols; ++c){
                if(board[r][c] == '.') continue;
                if(seen[board[r][c] - '0'] == 1) return false;
                ++seen[board[r][c] - '0'];
            }
        }

        for(int c=0; c<cols; ++c){
            int[] seen = new int[10];
            for(int r=0; r<rows; ++r){
                if(board[r][c] == '.') continue;
                if(seen[board[r][c] - '0'] == 1) return false;
                ++seen[board[r][c] - '0'];
            }
        }

        for(int s=0; s<9; ++s){
            int[] seen = new int[10];
            for(int r=0; r<3; ++r)
            for(int c=0; c<3; ++c){
                int row = (s / 3) * 3 + r, col = (s % 3) * 3 + c;
                if(board[row][col] == '.') continue;
                if(seen[board[row][col] - '0'] == 1) return false;
                ++seen[board[row][col] - '0'];
            }
        }

        return true;
    }
}