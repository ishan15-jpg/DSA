class Solution {
public:
    int maxProduct(vector<int>& nums) {
        size_t n = nums.size();
        int prefix = 1, suffix = 1, max_ = nums[0];
        for(int i=0;i<n;++i){
            prefix = nums[i] * (prefix == 0 ? 1 : prefix);
            suffix = nums[n-1-i] * (suffix == 0 ? 1 : suffix);
            max_ = max(max_,max(prefix,suffix));
        }
        return max_;
    }
};