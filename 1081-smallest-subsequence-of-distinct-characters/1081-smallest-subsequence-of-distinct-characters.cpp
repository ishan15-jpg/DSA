class Solution {
    bool isGreater(char a, char b){
        return a - 'a' > b - 'a';
    }

public:
    string smallestSubsequence(string s) {
        vector<int> lastOccurrence(26,-1);
        for(int i=0; i<s.length(); ++i)
            lastOccurrence[s[i] - 'a'] = i;
        vector<char> res;
        for(int i=0; i<s.length(); ++i){
            if(find(res.begin(),res.end(),s[i]) != res.end()) continue;
            while(!res.empty() && this->isGreater(res.back(),s[i]) && i < lastOccurrence[res.back()-'a'])
                res.pop_back();
            res.push_back(s[i]);
        }
        string ans;
        for(const char c : res) ans += c;
        return ans;
    }
};