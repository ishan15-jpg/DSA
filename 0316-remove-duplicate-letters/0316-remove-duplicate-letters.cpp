class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> lastOccurrence(26,-1);
        for(int i=0; i<s.length(); ++i) 
            lastOccurrence[s[i] - 'a'] = i;
        vector<char> ans;
        for(int i=0; i<s.length(); ++i){
            if(find(ans.begin(),ans.end(),s[i]) != ans.end()) continue;
            while(!ans.empty() && s[i] - 'a' < ans.back() - 'a' && i < lastOccurrence[ans.back() - 'a'])
                ans.pop_back();
            ans.push_back(s[i]);
        }
        string res = "";
        for(const char c : ans) res += c;
        return res;
    }
};