class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        int curr = startFuel;
        int pre = 0;
        int ans = 0;
        priority_queue<int> pq;
        stations.push_back({target,0});
        for(const vector<int> station : stations){
            int dist = station[0] - pre;
            curr -= dist;
            while(!pq.empty() and curr < 0){
                curr += pq.top(); pq.pop();
                ++ans;
            }
            if(pq.empty() and curr < 0) return -1;
            pq.push(station[1]);
            pre = station[0];
        }
        return ans;
    }
};