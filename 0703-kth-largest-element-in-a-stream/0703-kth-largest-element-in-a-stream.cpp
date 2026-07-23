class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(const int num : nums){ 
            this->pq.push(num);    
        }
        while(this->pq.size() > k) this->pq.pop();
    }
    
    int add(int val) {
        this->pq.push(val);
        if(this->pq.size() > k) this->pq.pop();
        return this->pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */