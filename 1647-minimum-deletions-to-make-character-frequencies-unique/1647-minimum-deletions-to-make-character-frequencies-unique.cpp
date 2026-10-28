class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26,0);
        for(const char c : s) ++freq[c - 'a'];
        priority_queue<int> pq;
        for(const int f : freq)
            if(f > 0) pq.push(f);
        int res = 0;
        while(pq.size() > 1){
            int a = pq.top(); pq.pop();
            int b = pq.top(); pq.pop();
            if(a == b){
                ++res;
                if(b-1 > 0) pq.push(b-1);
                pq.push(a);
            }else pq.push(b);
        }
        return res;
    }
};