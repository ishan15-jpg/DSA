class Solution {
public:
    int characterReplacement(string s, int k) {
        size_t n = s.length();
        int l = 0, maxFreq = 0, max_ = 0;
        vector<int> freq(26,0);
        for(int r=0; r<n; ++r){
            maxFreq = max(maxFreq, ++freq[s[r] - 'A']);
            while(l<=r && r-l+1-maxFreq > k){
                --freq[s[l] - 'A'];
                ++l;
            }
            max_ = max(max_, r-l+1);
        }
        return max_;
    }
};