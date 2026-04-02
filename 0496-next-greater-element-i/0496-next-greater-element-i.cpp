class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        size_t n1 = nums1.size(), n2 = nums2.size();

        vector<int> max_(10001, -1);
        stack<int> s;

        for(int i=n2-1; i>=0; i--){
            while(!s.empty() && nums2[i] >= s.top()) s.pop();

            if(!s.empty()) max_[nums2[i]] = s.top();
            s.push(nums2[i]);
        }

        for(int i=0; i<n1; i++) nums1[i] = max_[nums1[i]];

        return nums1;
    }
};