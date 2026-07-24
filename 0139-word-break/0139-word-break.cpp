class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        size_t l = s.length();

        vector<bool> dp(l+1, false);
        dp[l] = 1;

        for(int i=l-1; i>=0; --i){
            for(const string word : wordDict){
                int l_ = word.length();
                if(l-i < l_) continue;
                if(s.substr(i,l_) == word && dp[i+l_]) dp[i] = true;
            }
        }

        return dp[0];
    }
};