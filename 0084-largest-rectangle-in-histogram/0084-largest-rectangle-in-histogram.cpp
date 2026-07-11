class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        size_t n = heights.size();

        stack<pair<int,int>> st;
        int max_ = 0;

        for(int i=0; i<n; ++i){
            int start = i;
            while(!st.empty() && st.top().first >= heights[i]){
                auto [height,index] = st.top(); st.pop();
                max_ = max(max_, (i-index) * height);
                start = index;
            }
            st.push({heights[i],start});
        }

        while(!st.empty()){
            auto [height,index] = st.top(); st.pop();
            max_ = max(max_, ((int)n - index) * height);
        }

        return max_;
    }
};