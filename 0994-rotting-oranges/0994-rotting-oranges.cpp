class Solution {
    int directions[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};

public:
    int orangesRotting(vector<vector<int>>& grid) {
        size_t m = grid.size(), n = grid[0].size();

        if(m == 1 && n == 1){
            if(grid[0][0] == 0 || grid[0][0] == 2) return 0;
            if(grid[0][0] == 1) return -1;
        }

        function<bool(int,int)> isValid = [&](int row, int col) -> bool {
            return row >= 0 && row < m && col >= 0 && col < n;
        }; 

        queue<pair<int,int>> q;

        for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
        if(grid[i][j] == 2) q.push({i,j});

        int answer = 0;

        while(!q.empty()){
            int s = q.size();

            bool flag = false;
            for(int i=0; i<s; i++){
                auto [row,col] = q.front(); q.pop();

                for(int k=0; k<4; k++){
                    int neigh_row = row + directions[k][0], neigh_col = col + directions[k][1];

                    if(isValid(neigh_row,neigh_col) && grid[neigh_row][neigh_col] == 1){
                        grid[neigh_row][neigh_col] = 2;
                        q.push({neigh_row,neigh_col});
                        flag = true;
                    }
                }
            }

            if(flag) answer++;
        }

        for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
        if(grid[i][j] == 1) return -1;

        return answer;
    }
};