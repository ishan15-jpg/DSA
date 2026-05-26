class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        size_t m = matrix.size(), n = matrix[0].size();

        function<pair<int,int>(int)> help = [&](int k) -> pair<int,int> {
            int row = k / n, col = k % n;
            return {row,col};
        };

        int l = 0, r = m*n-1;

        while(l <= r){
            int mid = (l + r) >> 1;
            pair<int,int> cell = help(mid);

            if(matrix[cell.first][cell.second] == target) return true;
            else if(matrix[cell.first][cell.second] < target) l = mid + 1;
            else r = mid - 1;
        }

        return false;
    }
};