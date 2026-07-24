class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        size_t l = s.length();

        unordered_set<string> st;
        for(const string word : wordDict) st.insert(word);

        vector<int> dp(l+1, -1);
        dp[l] = 1;

        function<bool(int)> rec = [&](int i) -> bool {
            if(i >= l) return true;
            if(dp[i] != -1) return dp[i] == 1;

            for(int j=1; j<l-i+1; ++j){
                if(st.find(s.substr(i,j)) != st.end() && rec(i+j)){ 
                    dp[i] = 1;
                    return true;
                };
            }

            dp[i] = 0;
            return false;
        };

        return rec(0);
    }
};