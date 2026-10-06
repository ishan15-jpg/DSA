class Solution {
    unordered_map<char,string> mp = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        auto backtrack = [&](auto& self, int i, string& temp){
            if(i == digits.length()){
                res.push_back(temp);
                return;
            }
            for(const char c : this->mp[digits[i]]){
                temp.push_back(c);
                self(self, i+1, temp);
                temp.pop_back();
            }
        };
        string temp = "";
        backtrack(backtrack,0,temp);
        return res;
    }
};