class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        size_t n = heights.size();

        stack<int> nst; stack<int> pst;
        vector<int> nse(n,n); vector<int> pse(n,-1);

        for(int i=0; i<n; ++i){
            while(!pst.empty() && heights[i] <= heights[pst.top()]) pst.pop();
            if(!pst.empty()) pse[i] = pst.top();
            pst.push(i);

            while(!nst.empty() && heights[n-1-i] <= heights[nst.top()]) nst.pop();
            if(!nst.empty()) nse[n-1-i] = nst.top();
            nst.push(n-1-i);
        }

        int max_ = 0;

        for(int i=0; i<n; ++i){
            int left = pse[i]+1, right = nse[i]-1;
            max_ = max(max_, (right - left + 1) * heights[i]); 
        }

        return max_;
    }
};