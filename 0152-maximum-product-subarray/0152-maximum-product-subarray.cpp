class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_ = nums[max_element(nums.begin(),nums.end()) - nums.begin()];

        vector<vector<int>> segments;
        vector<int> temp;
        for(const int num : nums){
            if(num == 0){
                if(!temp.empty()){
                    segments.push_back(temp);
                    temp.clear();
                }
            }else temp.push_back(num);
        }
        segments.push_back(temp);

        for(const vector<int>& segment : segments){
            int prd = 1, negs = 0, i = 0;
            size_t n = segment.size();
            for(const int num : segment) if(num < 0) ++negs;
            int need = negs%2 == 0 ? negs : negs - 1;
            negs = 0;
            
            for(int j=0;j<n;++j){
                prd *= segment[j];
                if(segment[j] < 0){
                    ++negs;
                    while(negs > need){
                        prd /= segment[i];
                        if(segment[i] < 0) --negs;
                        ++i;
                    }
                }
                if(i<=j) max_ = max(max_, prd);
            }
        }

        return max_;
    }
};