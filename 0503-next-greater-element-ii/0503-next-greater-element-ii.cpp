class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        size_t n = nums.size();

        stack<int> st;

        for(int i=n-2; i>=0; i--){
            while(!st.empty() && nums[i] >= st.top()) st.pop();
            st.push(nums[i]);
        }

        for(int i=n-1; i>=0; i--){
            while(!st.empty() && nums[i] >= st.top()) st.pop();

            int temp = nums[i]; 
            if(!st.empty()) nums[i] = st.top();
            else nums[i] = -1;
            st.push(temp);
        }

        return nums;
    }
};