class Solution {
public:
    int maxProduct(vector<int>& nums) {
       int currMax = 1, currMin = 1, max_ = nums[0];

       for(const int num : nums){
            int temp = currMax * num;
            currMax = max(num, max(currMax*num, currMin*num));
            currMin = min(num, min(temp, currMin*num));
            max_ = max(max_,currMax);
       }

       return max_;
    }
};