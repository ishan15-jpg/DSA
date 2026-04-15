class Solution {
    int rows[4] = {1,0,-1,0};
    int cols[4] = {0,-1,0,1};

    bool isValid(int r, int c, int m, int n){
        return r>=0 && r<m && c>=0 && c<n;
    }

    void dfs(int i, int j, int m, int n, vector<vector<bool>>& mark, vector<vector<char>>& board){
        mark[i][j] = true;

        for(int k=0; k<4; k++)
        if(isValid(i+rows[k], j+cols[k], m, n) && board[i+rows[k]][j+cols[k]] == 'O' && mark[i+rows[k]][j+cols[k]] == false) dfs(i+rows[k],j+cols[k],m,n,mark,board);
    }

public:
    void solve(vector<vector<char>>& board) {
        size_t m = board.size(), n = board[0].size();

        vector<vector<bool>> mark(m, vector<bool>(n, false));

        for(int i=0; i<n; i++)
        if(board[0][i] == 'O' && mark[0][i] == false) dfs(0,i,m,n,mark,board);

        for(int i=1; i<m; i++)
        if(board[i][n-1] == 'O' && mark[i][n-1] == false) dfs(i,n-1,m,n,mark,board);

        for(int i=n-2; i>=0; i--)
        if(board[m-1][i] == 'O' && mark[m-1][i] == false) dfs(m-1,i,m,n,mark,board);

        for(int i=m-2; i>=1; i--)
        if(board[i][0] == 'O' && mark[i][0] == false) dfs(i,0,m,n,mark,board);

        for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
        if(board[i][j] == 'O' && mark[i][j] == false) board[i][j] = 'X';
    }
};