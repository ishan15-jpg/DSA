class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        size_t n = nums.size();
        vector<vector<int>> answer;
        function<void(int)> rec = [&](int i){
            if(i == n){ 
                answer.push_back(nums);
                return;
            }
            for(int j=i; j<n; ++j){
                swap(nums[i],nums[j]);
                rec(i+1);
                swap(nums[i],nums[j]);
            }
        };
        rec(0);
        return answer;
    }
};