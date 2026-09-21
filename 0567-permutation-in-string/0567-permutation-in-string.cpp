class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        size_t l1 = s1.length(), l2 = s2.length();
        if(l1 > l2) return false;
        array<int,26> count1 = {0}, count2 = {0};
        for(int i=0; i<l1; ++i){
            ++count1[s1[i] - 'a'];
            ++count2[s2[i] - 'a'];
        }
        if(count1 == count2) return true;
        for(int i=l1; i<l2; ++i){
            ++count2[s2[i] - 'a'];
            --count2[s2[i-l1] - 'a'];
            if(count2 == count1) return true;
        }
        return false;
    }
};