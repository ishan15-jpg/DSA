class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        if(n == 1) return {0};

        stack<pair<int,int>> st;
        vector<int> answer(n, 0);

        for(int i=n-1; i>=0; i--){
            while(!st.empty() && temperatures[i] >= st.top().first) st.pop();

            if(!st.empty()) answer[i] = st.top().second - i;
            st.push({temperatures[i], i});
        }

        return answer;
    }
};