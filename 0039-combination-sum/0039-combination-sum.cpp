class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        size_t n = candidates.size();

        vector<vector<int>> answer;
        vector<int> temp;

        function<void(int,int)> backtrack = [&](int i, int sum){
            if(sum == target){
                answer.push_back(temp);
                return;
            }
            if(sum > target || i == n) return;

            temp.push_back(candidates[i]);
            backtrack(i,sum+candidates[i]);
            temp.pop_back();
            backtrack(i+1,sum);
        };

        backtrack(0,0);

        return answer;
    }
};