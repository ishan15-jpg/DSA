class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        size_t n = nums.size();

        vector<int> answer(n, 0);
        vector<int> prefix(n, 1);
        vector<int> suffix(n, 1);

        for(int i=1; i<n; ++i){
            prefix[i] = prefix[i-1] * nums[i-1];
            suffix[n-1-i] = suffix[n-i] * nums[n-i];
        }

        for(int i=0; i<n; ++i) answer[i] = prefix[i] * suffix[i];

        return answer;
    }
};