class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq;
        for(const int num : nums) pq.push(num);
        int res = pq.top();
        while(k--){
            res = pq.top();
            pq.pop();
        }
        return res;
    }
};