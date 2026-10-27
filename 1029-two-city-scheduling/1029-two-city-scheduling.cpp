class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(),costs.end(), [](vector<int>&a,vector<int>&b){
            return a[0]-a[1] < b[0]-b[1];
        });
        int n = costs.size() / 2;
        int res = 0;
        for(int i=0; i<costs.size(); ++i){
            if(i < n) res += costs[i][0];
            else res += costs[i][1];
        }
        return res;
    }
};