class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        size_t n = nums.size();

        sort(nums.begin(), nums.end());

        vector<vector<int>> answer;

        unordered_map<int,int> mp;
        for(const int num : nums) mp[num]++;

        for(int i=0; i<n-1; ++i){
            --mp[nums[i]];
            if(i > 0 && nums[i] == nums[i-1]) continue;
            for(int j=i+1; j<n; ++j){
                --mp[nums[j]];
                if(j-1 > i && nums[j] == nums[j-1]) continue;
                int target = -(nums[i] + nums[j]);
                if(mp.find(target) != mp.end() && mp[target] > 0) answer.push_back({nums[i],nums[j],target});
            }
            for(int j=i+1; j<n; ++j) ++mp[nums[j]];
        }

        return answer;
    }
};