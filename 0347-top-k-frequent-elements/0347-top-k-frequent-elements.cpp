class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        size_t n = nums.size();

        unordered_map<int,int> mp;
        for(const int num : nums) mp[num]++;

        vector<vector<int>> bucket(n+1);

        for(const auto &it : mp) bucket[it.second].push_back(it.first);

        vector<int> answer;
        for(int i=n; i>=0; i--){
            for(const int i : bucket[i]){
                answer.push_back(i);
                if(answer.size() == k) return answer;
            }
        }
        
        return answer;
    }
};