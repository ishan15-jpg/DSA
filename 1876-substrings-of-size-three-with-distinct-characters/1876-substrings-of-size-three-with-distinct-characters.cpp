class Solution {
public:
    int countGoodSubstrings(string s) {
        size_t n = s.length();

        if(n < 3) return 0;

        short int count = 0;

        for(int i=0; i<n-2; i++)
        if(s[i] != s[i+1] && s[i+1] != s[i+2] && s[i+2] != s[i]) count++;

        return int(count);
    }
};