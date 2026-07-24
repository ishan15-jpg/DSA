class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        size_t l = s.length();

        vector<int> dp(l+1, -1);
        dp[l] = 1;

        function<bool(int)> rec = [&](int i) -> bool {
            if(i >= l) return true;
            if(dp[i] != -1) return dp[i] == 1;

            for(const string word : wordDict){
                size_t l_ = word.length();
                if(l - i < l_) continue;
                if(s.substr(i,l_) == word && rec(i+l_)){
                    dp[i] = 1;
                    return true;
                }
            }

            dp[i] = 0;
            return false;
        };

        return rec(0);
    }
};