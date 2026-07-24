class Solution {
public:
    vector<int> countBits(int n) {
        if(n == 0) return {0};
        vector<int> ans{0,1};

        function<int(unsigned int)> countOnes = [&](unsigned int i) -> int {
            int count = 0;
            while(i){
                i &= i-1;
                ++count;
            }
            return count;
        };

        for(unsigned int i=2; i<n+1; ++i){
            ans.push_back(countOnes(i));
        }

        return ans;
    }
};