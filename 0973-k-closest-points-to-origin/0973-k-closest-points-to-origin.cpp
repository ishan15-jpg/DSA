class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int,vector<int>>, vector<pair<int,vector<int>>>, greater<pair<int,vector<int>>>> pq;
        for(const vector<int> point : points){
            int distance = point[0]*point[0] + point[1]*point[1];
            pq.push({distance,point});
        }
        vector<vector<int>> res;
        while(k--){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};