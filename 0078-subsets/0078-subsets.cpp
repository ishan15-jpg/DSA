class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        size_t n = nums.size();

        if(n == 1) return {{},{nums[0]}};

        vector<vector<int>> answer{{}};

        for(int i=1; i<(1 << n); ++i){
            vector<int> temp;
            for(int j=0; j<n; ++j){
                if((1 << j) & i) temp.push_back(nums[j]);
            }
            answer.push_back(temp);
        }

        return answer;
    }
};