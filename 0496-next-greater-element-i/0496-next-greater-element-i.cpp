class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        size_t n1 = nums1.size(), n2 = nums2.size();

        for(int i=0; i<n1; i++){
            int max_ = -1;
            for(int j=0; j<n2; j++){
                if(nums1[i] == nums2[j]){
                    for(int k=j+1; k<n2; k++){
                        if(nums2[k] > nums2[j]){
                            max_ = nums2[k];
                            break;
                        }
                    }
                }
            }
            nums1[i] = max_;
        }

        return nums1;
    }
};