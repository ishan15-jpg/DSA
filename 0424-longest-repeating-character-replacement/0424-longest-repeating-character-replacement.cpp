class Solution {
public:
    int characterReplacement(string s, int k) {
        size_t n = s.length();
        unordered_set<int> st;
        for(const char c : s) st.insert(c - 'A');
        int max_ = 0;
        for(const int c : st){
            vector<int> freq(26,0);
            int maxFreq = 0, l = 0;
            for(int r=0; r<n; ++r){
                ++freq[s[r] - 'A'];
                maxFreq = max(maxFreq, freq[c]);
                while(l<=r && r-l+1-maxFreq > k){
                    --freq[s[l] - 'A'];
                    ++l; 
                }
                max_ = max(max_, r-l+1);
            }
        }
        return max_;
    }
};