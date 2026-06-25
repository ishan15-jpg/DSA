class Solution {
public:
    int numDecodings(string s) {
        size_t n = s.length();

        vector<int> dp(n+1, 0);

        dp[n] = 1;

        for(int i=n-1; i>=0; --i){
            if(s[i] == '0') continue;

            int one = dp[i+1];
            
            int two = 0;
            if(i+2 <= n){
                int num = stoi(s.substr(i,2));
                two = (num >= 10 && num <= 26) ? dp[i+2] : 0;
            }

            dp[i] = one + two;
        }        

        return dp[0];
    }
};