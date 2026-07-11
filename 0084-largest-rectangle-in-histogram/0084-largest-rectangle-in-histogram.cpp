class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        size_t n = heights.size();

        int max_ = 0;
        stack<int> st;

        for(int i=0; i<n+1; ++i){
            while(!st.empty() && (i == n || heights[i] <= heights[st.top()])){
                int height = heights[st.top()]; st.pop();
                int width = st.empty() ? i : i - st.top() - 1;
                max_ = max(max_, height * width);
            }
            st.push(i);
        }

        return max_;
    }
};