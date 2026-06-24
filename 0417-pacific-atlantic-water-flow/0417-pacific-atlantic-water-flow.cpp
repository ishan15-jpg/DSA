class Solution {
    int directions[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        size_t rows = heights.size(), cols = heights[0].size();

        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));

        function<void(int,int,int,vector<vector<bool>>&)> dfs = [&](int row, int col, int prev, vector<vector<bool>>& ocean){
            if(row < 0 || col < 0 || row == rows || col == cols || ocean[row][col] || heights[row][col] < prev) return;

            ocean[row][col] = true;
            for(int k=0; k<4; k++) dfs(row+directions[k][0], col+directions[k][1], heights[row][col], ocean);
        };

        for(int i=0; i<rows; i++){
            dfs(i,0,heights[i][0],pacific);
            dfs(i,cols-1,heights[i][cols-1],atlantic);
        }

        for(int i=0; i<cols; i++){
            dfs(0,i,heights[0][i],pacific);
            dfs(rows-1,i,heights[rows-1][i],atlantic);
        }

        vector<vector<int>> answer;

        for(int r=0; r<rows; r++)
        for(int c=0; c<cols; c++)
        if(pacific[r][c] && atlantic[r][c]) answer.push_back({r,c});

        return answer;
    }
};