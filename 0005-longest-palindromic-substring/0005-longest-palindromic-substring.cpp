class Solution {
public:
    string longestPalindrome(string s) {
        size_t n = s.length();

        vector<vector<bool>> dp(n+1, vector<bool>(n+1, false));

        string answer = "";
        int max_ = 0;

        for(int i=n-1; i>=0; --i)
        for(int j=i; j<n; ++j){
            if(s[i] == s[j] && (j-i+1 <= 3 || dp[i+1][j-1])){
                dp[i][j] = true;
                if(j-i+1 > max_){
                    max_ = j-i+1;
                    answer = s.substr(i,j-i+1);
                }
            }
        }

        return answer;
    }
};