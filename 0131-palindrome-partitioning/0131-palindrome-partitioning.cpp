class Solution {
public:
    vector<vector<string>> partition(string s) {
        size_t l = s.length();
        vector<vector<bool>> dp(l,vector<bool>(l,false));
        for(int i=l-1;i>=0;--i){
            for(int j=i; j<l; ++j){
                if(s[j] == s[i] and (j-i+1 <= 3 or dp[i+1][j-1]))
                    dp[i][j] = true;
            }
        }
        vector<vector<string>> answer;
        vector<string> temp;
        auto backtrack = [&](auto& self, int i) -> void {
            if(i == l){
                answer.push_back(temp);
                return;
            }
            for(int j=i; j<l; ++j){
                if(dp[i][j]){
                    temp.push_back(s.substr(i,j-i+1));
                    self(self,j+1);
                    temp.pop_back();
                }
            }
        };
        backtrack(backtrack,0);
        return answer;
    }
};