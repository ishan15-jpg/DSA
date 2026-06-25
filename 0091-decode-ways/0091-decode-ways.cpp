class Solution {
public:
    int numDecodings(string s) {
        size_t n = s.length();

        int dp = 0, dp1 = 1, dp2 = 0;

        for(int i=n-1; i>=0; --i){
            if(s[i] == '0') dp = 0;
            else dp = dp1;
            
            if(i+2 <= n){
                int num = stoi(s.substr(i,2));
                dp += (num >= 10 && num <= 26) ? dp2 : 0;
            }

            dp2 = dp1;
            dp1 = dp;
            dp = 0;
        }        

        return dp1;
    }
};