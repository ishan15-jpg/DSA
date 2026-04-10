class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        if(n == 1) return {0};

        stack<int> st;
        vector<int> answer(n, 0);

        for(int i=0; i<n; ++i){
            while(!st.empty() && temperatures[i] > temperatures[st.top()]){
                answer[st.top()] = i - st.top();
                st.pop();
            }

            st.push(i);
        }

        return answer;
    }
};