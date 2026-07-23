class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        size_t n = candidates.size();

        vector<vector<int>> answer;
        vector<int> temp;

        function<void(int,int)> rec = [&](int i, int t){
            if(i == n || t < 0) return;
            if(t == 0){
                answer.push_back(temp);
                return;
            }
            temp.push_back(candidates[i]);
            rec(i, t-candidates[i]);
            temp.pop_back();
            rec(i+1, t);
        };

        rec(0,target);

        return answer;
    }
};