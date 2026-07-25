class Solution {
    bool dfs(int i, int j, int k, string& word, vector<vector<char>>& board){
        if(k == word.length()) return true;

        if(i < 0 || j < 0 || i == board.size() || j == board[0].size() || board[i][j] != word[k] || board[i][j] == '!') return false;

        char temp = board[i][j];
        board[i][j] = '!';

        bool left = dfs(i-1,j,k+1,word,board);
        bool top = dfs(i,j+1,k+1,word,board);
        bool right = dfs(i+1,j,k+1,word,board);
        bool bottom = dfs(i,j-1,k+1,word,board);

        board[i][j] = temp;
        return left || top || right || bottom;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        size_t m = board.size(), n = board[0].size(), l = word.length();

        for(int i=0; i<m; ++i)
        for(int j=0; j<n; ++j)
        if(board[i][j] == word[0] && dfs(i,j,0,word,board)) return true;

        return false; 
    }
};