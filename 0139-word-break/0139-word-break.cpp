class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        size_t l = s.length();

        unordered_set<string> st;
        for(const string word : wordDict) st.insert(word);

        vector<bool> dp(l+1, false);
        dp[l] = 1;

        for(int i=l-1; i>=0; --i){
            for(int j=1; j<l-i+1; ++j){
                if(st.find(s.substr(i,j)) != st.end() && dp[i+j]) dp[i] = true;
            }
        }

        return dp[0];
    }
};