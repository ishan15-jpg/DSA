class LRUCache {
    int capacity;
    vector<pair<int,int>> store;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        int idx = -1;
        for(int i=0; i<this->store.size(); ++i)
        if(this->store[i].first == key){ 
            idx = i;
            break;
        }
        if(idx == -1) return -1;
        pair<int,int> tmp = this->store[idx];
        this->store.erase(this->store.begin()+idx);
        this->store.push_back(tmp);
        return tmp.second;
    }
    
    void put(int key, int value) {
        int idx = -1;
        for(int i=0; i<this->store.size(); ++i)
        if(this->store[i].first == key){
            idx = i;
            break;
        }
        if(idx != -1) this->store.erase(this->store.begin()+idx);
        if(this->store.size() == this->capacity) this->store.erase(this->store.begin());
        this->store.push_back({key,value});
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */