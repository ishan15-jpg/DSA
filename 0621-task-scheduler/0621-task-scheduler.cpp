class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26,0);
        for(const char& task : tasks) ++freq[task - 'A'];
        priority_queue<int> pq;
        for(const int& f : freq) 
            if(f > 0) pq.push(f);
        int res = 0;
        while(!pq.empty()){
            vector<int> temp;
            for(int i=0; i<n+1; ++i){
                if(pq.empty()) break;
                int f = pq.top(); pq.pop();
                temp.push_back(f-1);
            }
            for(const int& f : temp){
                if(f > 0) pq.push(f);
            }
            if(pq.empty()) res += temp.size();
            else res += n+1;
        }
        return res;
    }
};