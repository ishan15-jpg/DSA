class Solution {
public:
    int rob(vector<int>& nums) {
        size_t n = nums.size();

        if(n == 1) return nums[0];
        if(n == 2) return max(nums[0], nums[1]);

        int next = 0, next1 = 0, curr0 = 0;

        for(int i=n-2; i>=0; --i){
            curr0 = max(nums[i]+next1, next);
            next1 = next;
            next = curr0;
        }

        next = 0; next1 = 0;
        int curr1 = 0;
        for(int i=n-1; i>=1; --i){
            curr1 = max(nums[i]+next1, next);
            next1 = next;
            next = curr1;
        }

        return max(curr1, curr0);
    }
};