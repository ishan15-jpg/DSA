class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        size_t n = nums.size();

        vector<vector<int>> answer;
        vector<int> temp;

        function<void(int)> backtrack = [&](int i){
            if(i == n){
                answer.push_back(temp);
                return;
            }
            temp.push_back(nums[i]);
            backtrack(i+1);
            temp.pop_back();
            backtrack(i+1);
        };

        backtrack(0);

        return answer;
    }
};