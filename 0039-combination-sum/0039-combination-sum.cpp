class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        size_t n = candidates.size();

        vector<vector<int>> answer;
        vector<int> temp;

        sort(candidates.begin(), candidates.end());

        function<void(int,int)> rec = [&](int i, int t){
            if(i == n || t < 0) return;
            if(t == 0){
                answer.push_back(temp);
                return;
            }
            for(int j=i; j<n; ++j){
                if(t - candidates[j] < 0) return;
                temp.push_back(candidates[j]);
                rec(j, t-candidates[j]);
                temp.pop_back();
            }
        };

        rec(0,target);

        return answer;
    }
};